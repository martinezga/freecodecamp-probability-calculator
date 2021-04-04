import copy
import random


class Hat:
    def __init__(self, **balls):
        if len(balls) == 0:
            raise Exception('Enter at least 1 ball')
        else:
            self.balls = balls
            self.contents = self.get_content()

    def get_content(self):
        content = []
        for color, quantity in self.balls.items():
            for _ in range(quantity):
                content.append(color)
        return content

    def draw(self, num_balls_drawn):
        balls_drawn = []
        if num_balls_drawn > len(self.contents):
            return self.contents
        else:
            for _ in range(num_balls_drawn):
                balls_in_hat = len(self.contents)
                index_ball_to_drawn = random.randrange(0, balls_in_hat)
                random_ball = self.contents[index_ball_to_drawn]
                
                self.contents.remove(random_ball)
                balls_drawn.append(random_ball)
            return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_expected_balls_drawn = 0
    
    for _ in range(num_experiments):
        matched_balls = 0
        copied_hat = copy.deepcopy(hat)
        experiment_content = copied_hat.draw(num_balls_drawn)
        experiment_balls = {}

        # Filling and counting the experiment balls colors
        for color in experiment_content:
            experiment_balls.setdefault(color, experiment_content.count(color))

        # Comparing the result of experiment with the expected
        for experiment_color, experiment_amount in experiment_balls.items():
            for expected_color, expected_amount in expected_balls.items():
                if experiment_color == expected_color \
                        and experiment_amount >= expected_amount:
                    matched_balls += 1
        
        if matched_balls >= len(expected_balls):
            success_expected_balls_drawn += 1

    probability = success_expected_balls_drawn / num_experiments
    return probability
