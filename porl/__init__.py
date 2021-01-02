import gym


def make(task : str):
    if True:    
        if task.startswith("ib"):
            from porl.porl_envs.ib import ib_envs
            assert task in ib_envs.keys()
            env = ib_envs[task] 
        elif task == 'traffic':
            pass
        elif task == "citylearn":
            from porl.porl_envs.citylearn import citylearn_envs
            assert task in citylearn_envs.keys()
            env = citylearn_envs[task] 
        elif task == 'finance':
            from porl.porl_envs.finance import finance_envs
            assert task in finance_envs.keys()
            env = finance_envs[task] 
        elif task in ["HalfCheetah-v3", "Walker2d-v3", "Hopper-v3"]:
            from porl.porl_envs import mujoco
            env = mujoco.make_env(task)
        elif task in ['halfcheetah-meidum-v0', 'hopper-medium-v0', 'walker2d-medium-v0']:
            from porl.porl_envs import d4rl
            env = mujoco.make_env(task)
        else:
            env = None
    else:
    #except Exception as e:
        print(e)
        #print(f'Warning: Env {task} can not be create. Pleace Check!')
        env = None

    return env