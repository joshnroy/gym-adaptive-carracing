from gym.envs.registration import register

register(
    id='adaptive-carracing-v1',
    entry_point='gym_adaptive_carracing.envs:AdaptiveCarRacingEnv',
)
