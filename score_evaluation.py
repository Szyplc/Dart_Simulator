from config import *
import math

def evaluate_score(pos: tuple[float, float]) -> int:
        dx = pos[0] - CENTER[0]
        dy = pos[1] - CENTER[1]
        distance = (dx**2 + dy**2)**0.5
    
        if distance <= R_BULL_IN:
            return 50
        elif distance <= R_BULL_OUT:
            return 25
    
        value = BOARD_VALUES[int(((((math.atan2(dy, dx) + math.pi) / math.pi * 10 + 0.5) % 20) - 5) % 20)]
        if R_TRIPLE_IN < distance <= R_TRIPLE_OUT:
            return value * 3
    
        if R_DOUBLE_IN < distance <= R_DOUBLE_OUT:
            return value * 2
    
        if distance <= R_DOUBLE_IN:
            return value
    
        return 0