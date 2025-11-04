
from dataclasses import dataclass
from typing import List

import numpy as np

@dataclass
class VehicleState:

    frame_id: int
    vehicle_id: int
    x: float  # 位置 x
    y: float  # 位置 y
    vx: float # 速度 vx
    vy: float # 速度 vy
    length: float # 车辆长度
    width: float  # 车辆宽度
    heading: float # 车辆航向角
    
    @property
    def speed(self) -> float:
        return np.sqrt(self.vx ** 2 + self.vy ** 2)

    @property
    def phiv_a(self) -> float:
        return (np.pi / 180) * self.heading

    def to_array(self) -> np.ndarray:
        return np.array([self.frame_id, self.vehicle_id, self.x, self.y,
                         self.length, self.width, self.vx, self.vy, self.heading])
    
@dataclass
class VehicleTrajectory:

    vehicle_id: int
    states: List[VehicleState] # 车辆状态列表

    def add_sigle_frame(self, state: VehicleState):
        self.states.append(state)

    def get_single_frame(self, frame_id: int) -> VehicleState:
        """
        获取某一帧的车辆状态
        """
        for state in self.states:
            if state.frame_id == frame_id:
                return state
        raise ValueError(f"Frame ID {frame_id} not found for vehicle ID {self.vehicle_id}")
    
    def get_frames(self, start_frame: int, end_frame: int) -> List[VehicleState]:
        """
        获取某一范围内的车辆状态列表
        """
        return [state for state in self.states if start_frame <= state.frame_id <= end_frame]

