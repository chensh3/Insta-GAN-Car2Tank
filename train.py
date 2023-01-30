import time
from options.train_options import TrainOptions
from data import CreateDataLoader
from models import create_model
from util.visualizer import Visualizer
from torch import rand
import time
from os import popen


def check_mem():
    mem = popen(
        '"nvidia-smi" --query-gpu=memory.total,memory.used --format=csv,nounits,noheader').read().split(
        ",")

    return mem


def memory_save():
    total, used = check_mem()

    total = int(total)
    used = int(used)

    max_mem = int(total * 0.5)
    block_mem = max_mem - used

    x = rand((256, 1024, block_mem), device="cuda")
    x = rand((2, 2), device="cuda")

    # do things here


def main(opt, dataset, dataset_size):
    model = create_model(opt)
    model.setup(opt)
    # opt.model.
    visualizer = Visualizer(opt)
    total_steps = 0

    # memory_save()

    for epoch in range(opt.epoch_count, opt.niter + opt.niter_decay + 1):
        t = time.localtime()
        current_time = time.strftime("%D %H:%M:%S", t)
        print('start of epoch %d / %d at %s' %
              (epoch, opt.niter + opt.niter_decay, current_time))
        epoch_start_time = time.time()
        iter_data_time = time.time()
        epoch_iter = 0

        for i, data in enumerate(dataset):
            iter_start_time = time.time()
            if total_steps % opt.print_freq == 0:
                t_data = iter_start_time - iter_data_time
            visualizer.reset()
            total_steps += opt.batch_size
            epoch_iter += opt.batch_size
            model.set_input(data)
            model.optimize_parameters()

            if total_steps % opt.display_freq == 0:
                save_result = total_steps % opt.update_html_freq == 0
                visualizer.display_current_results(model.get_current_visuals(), epoch, save_result)

            if total_steps % opt.print_freq == 0:
                losses = model.get_current_losses()
                t = (time.time() - iter_start_time) / opt.batch_size
                visualizer.print_current_losses(epoch, epoch_iter, losses, t, t_data)
                if opt.display_id > 0:
                    visualizer.plot_current_losses(epoch, float(epoch_iter) / dataset_size, opt, losses)

            if total_steps % opt.save_latest_freq == 0:
                print('saving the latest model (epoch %d, total_steps %d)' % (epoch, total_steps))
                save_suffix = 'iter_%d' % total_steps if opt.save_by_iter else 'latest'
                model.save_networks(save_suffix)

            iter_data_time = time.time()
        if epoch % opt.save_epoch_freq == 0:
            print('saving the model at the end of epoch %d, iters %d' % (epoch, total_steps))
            model.save_networks('latest')
            model.save_networks(epoch)
        t = time.localtime()
        current_time = time.strftime("%D %H:%M:%S", t)
        print('End of epoch %d / %d \t Time Taken: %d sec \t current time: %s' %
              (epoch, opt.niter + opt.niter_decay, time.time() - epoch_start_time, current_time))
        model.update_learning_rate()


if __name__ == '__main__':
    """
    grid search command:
    python train.py --dataroot ./datasets/car2tank --model insta_gan --name car2tank_instagan --loadSizeH 128 --loadSizeW 128 --lamb
da_A 0 --lambda_B 0 --lambda_idt 0 --lambda_ctx 0 --display_env 0_0_0 --checkpoints_dir ./checkpoints/0_0_0 --serial_batches

    """
    from grid_search import list_options

    grid_search = False
    # torch.cuda.empty_cache()
    # torch.cuda.set_per_process_memory_fraction(1., 0)

    opt = TrainOptions().parse()
    data_loader = CreateDataLoader(opt)
    dataset = data_loader.load_data()
    dataset_size = len(data_loader)
    print('#training images = %d' % dataset_size)
    # print(opt.lambda_A)
    # main(opt,dataset,dataset_size)
    if grid_search:
        for dict_option in list_options:
            print(
                f"was opt variables: A= {opt.lambda_A}, B= {opt.lambda_B}, idt= {opt.lambda_idt}, ctx= {opt.lambda_ctx}")
            opt.lambda_A = dict_option["lambda_A"]
            opt.lambda_B = dict_option["lambda_A"]
            opt.lambda_idt = dict_option["lambda_idt"]
            opt.lambda_ctx = dict_option["lambda_ctx"]
            opt.display_env = f"{dict_option['lambda_A']}_{dict_option['lambda_idt']}_{dict_option['lambda_ctx']}"
            opt.checkpoints_dir = f"./checkpoints/{dict_option['lambda_A']}_{dict_option['lambda_idt']}_{dict_option['lambda_ctx']}"

            print(
                f"changes opt variables: A= {opt.lambda_A}, B= {opt.lambda_B}, idt= {opt.lambda_idt}, ctx= {opt.lambda_ctx}")
            data_loader = CreateDataLoader(opt)
            dataset = data_loader.load_data()
            dataset_size = len(data_loader)
            print('#training images = %d' % dataset_size)
            main(opt, dataset, dataset_size)

    else:
        main(opt, dataset, dataset_size)
