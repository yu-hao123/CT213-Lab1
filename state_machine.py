import random
import math
from constants import *


class FiniteStateMachine(object):
    """
    A finite state machine.
    """
    def __init__(self, state):
        self.state = state

    def change_state(self, new_state):
        self.state = new_state

    def update(self, agent):
        self.state.check_transition(agent, self)
        self.state.execute(agent)


class State(object):
    """
    Abstract state class.
    """
    def __init__(self, state_name):
        """
        Creates a state.

        :param state_name: the name of the state.
        :type state_name: str
        """
        self.state_name = state_name

    def check_transition(self, agent, fsm):
        """
        Checks conditions and execute a state transition if needed.

        :param agent: the agent where this state is being executed on.
        :param fsm: finite state machine associated to this state.
        """
        raise NotImplementedError("This method is abstract and must be implemented in derived classes")

    def execute(self, agent):
        """
        Executes the state logic.

        :param agent: the agent where this state is being executed on.
        """
        raise NotImplementedError("This method is abstract and must be implemented in derived classes")


class MoveForwardState(State):
    def __init__(self):
        super().__init__("MoveForward")
        # Todo: add initialization code
        self.elapsed_time = 0

    def check_transition(self, agent, state_machine):
        # Todo: add logic to check and execute state transition
        if(self.elapsed_time > MOVE_FORWARD_TIME):
            state_machine.change_state(MoveInSpiralState())
        elif(agent.get_bumper_state()):
            state_machine.change_state(GoBackState())
        pass

    def execute(self, agent):
        # Todo: add execution logic
        agent.set_velocity(FORWARD_SPEED, 0)
        self.elapsed_time += SAMPLE_TIME
        pass


class MoveInSpiralState(State):
    def __init__(self):
        super().__init__("MoveInSpiral")
        # Todo: add initialization code
        self.elapsed_time = 0
    
    def check_transition(self, agent, state_machine):
        # Todo: add logic to check and execute state transition
        if(self.elapsed_time > MOVE_IN_SPIRAL_TIME):
            state_machine.change_state(MoveForwardState())
        elif(agent.get_bumper_state()):
            state_machine.change_state(GoBackState())
        pass

    def execute(self, agent):
        # Todo: add execution logic
        spiral_radius = INITIAL_RADIUS_SPIRAL + SPIRAL_FACTOR * self.elapsed_time
        angular_speed = FORWARD_SPEED/(spiral_radius)
        agent.set_velocity(FORWARD_SPEED, angular_speed)
        self.elapsed_time += SAMPLE_TIME
        pass


class GoBackState(State):
    def __init__(self):
        super().__init__("GoBack")
        # Todo: add initialization code
        self.elapsed_time = 0

    def check_transition(self, agent, state_machine):
        # Todo: add logic to check and execute state transition
        if(self.elapsed_time > GO_BACK_TIME):
            state_machine.change_state(RotateState())
        pass

    def execute(self, agent):
        # Todo: add execution logic
        agent.set_velocity(BACKWARD_SPEED, 0)
        self.elapsed_time += SAMPLE_TIME
        pass


class RotateState(State):
    def __init__(self):
        super().__init__("Rotate")
        # Todo: add initialization code
        self.elapsed_time = 0
        self.random_angle = random.randint(90, 270)

    def check_transition(self, agent, state_machine):
        # Todo: add logic to check and execute state transition
        rotation_time = self.random_angle*3.14)/(180*ANGULAR_SPEED
        if(self.elapsed_time > rotation_time):
            state_machine.change_state(MoveForwardState())
        pass
    
    def execute(self, agent):
        # Todo: add execution logic
        agent.set_velocity(0, ANGULAR_SPEED)
        self.elapsed_time += SAMPLE_TIME
        pass
