import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Training Config', add_help=False)
    parser.add_argument('-c', '--config', type=str, default='',
                        help='YAML config file specifying default arguments (default='')')
    # modelarts
    group = parser.add_argument_group('modelarts')
    group.add_argument('--enable_modelarts', type=bool, default=False,
                       help='Run on modelarts platform (default=False)')
    group.add_argument('--device_target', type=str, default='Ascend',
                       help='Target device, only used on modelarts platform (default=Ascend)')
    group.add_argument('--multi_data_url', type=str, default='/cache/data/',
                       help='path to multi dataset')
    group.add_argument('--data_url', type=str, default='/cache/data/',
                       help='path to dataset')
    group.add_argument('--ckpt_url', type=str, default='/cache/output/',
                       help='pre_train_model path in obs')
    group.add_argument('--train_url', type=str, default='/cache/output/',
                       help='model folder to save/load')

    args = parser.parse_args()

    return args


