import unittest
import random
import pygame
from snake_game import SnakeGame, Direction, Point, BLOCK_SIZE


# rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

BLOCK_SIZE = 20
SPEED = 10




font = pygame.font.Font('arial.ttf', 25)


class TestSnakeGame(unittest.TestCase):
 def setUp(self):
     self.game = SnakeGame()
     pygame.init()

 def test__(self):
        self.assertEqual(self.game.w, 640)
        self.assertEqual(self.game.h, 480)

       
        self.assertIsNotNone(self.game.display)
        self.assertIsNotNone(self.game.clock)

        
        self.assertEqual(self.game.direction, Direction.RIGHT)

        
        self.assertEqual(len(self.game.snake), 3)
        self.assertEqual(self.game.snake[0], self.game.head)
        self.assertEqual(self.game.snake[1], Point(self.game.head.x - BLOCK_SIZE, self.game.head.y))
        self.assertEqual(self.game.snake[2], Point(self.game.head.x - (2 * BLOCK_SIZE), self.game.head.y))

        
        self.assertEqual(self.game.score, 0)
        self.assertIsNotNone(self.game.food)

 class TestPlaceFood(unittest.TestCase):

    def setUp(self):
        self.game = SnakeGame()

    def test_place_food(self):
        
        
        self.game.snake = [Point(0, 0), Point(20, 0), Point(40, 0)]

        
        self.game._place_food()

        
        self.assertIsInstance(self.game.food, Point)

        
        self.assertLessEqual(self.game.food.x, self.game.w - BLOCK_SIZE)
        self.assertLessEqual(self.game.food.y, self.game.h - BLOCK_SIZE)

        
        self.assertEqual(self.game.food.x % BLOCK_SIZE, 0)
        self.assertEqual(self.game.food.y % BLOCK_SIZE, 0)

        
        self.assertNotIn(self.game.food, self.game.snake)

class TestPlayStep(unittest.TestCase):

    



    def setUp(self):
        # Set up the SnakeGame instance for testing
        self.game = SnakeGame()

    def test_collision_with_boundary(self):
        # Test whether _is_collision correctly detects collision with the boundary

        # Move the snake head outside the boundary
        self.game.head = Point(-1, 0)

        # Call the _is_collision method
        result = self.game._is_collision()

        # Check that collision is detected
        self.assertTrue(result)

    def test_collision_with_itself(self):
        # Test whether _is_collision correctly detects collision with itself

        # Move the snake head to a position where it collides with the snake body
        self.game.snake = [Point(0, 0), Point(20, 0), Point(20, 20)]
        self.game.head = Point(20, 0)

        # Call the _is_collision method
        result = self.game._is_collision()

        # Check that collision is detected
        self.assertTrue(result)

    def test_no_collision(self):
        # Test whether _is_collision correctly detects no collision

        # Move the snake head to a position where there is no collision
        self.game.snake = [Point(0, 0), Point(20, 0), Point(20, 20)]
        self.game.head = Point(40, 40)

        # Call the _is_collision method
        result = self.game._is_collision()

        # Check that no collision is detected
        self.assertFalse(result)       

class TestMove(unittest.TestCase):

    def setUp(self):
        # Set up the SnakeGame instance for testing
        self.game = SnakeGame()

    def test_move_right(self):
        # Test whether _move correctly updates the position for Direction.RIGHT

        # Set the initial position of the snake head
        self.game.head = Point(0, 0)

        # Call the _move method with Direction.RIGHT
        self.game._move(Direction.RIGHT)

        # Check that the head is moved to the right by BLOCK_SIZE
        self.assertEqual(self.game.head, Point(BLOCK_SIZE, 0))

    def test_move_left(self):
        # Test whether _move correctly updates the position for Direction.LEFT

        # Set the initial position of the snake head
        self.game.head = Point(BLOCK_SIZE, 0)

        # Call the _move method with Direction.LEFT
        self.game._move(Direction.LEFT)

        # Check that the head is moved to the left by BLOCK_SIZE
        self.assertEqual(self.game.head, Point(0, 0))

    def test_move_down(self):
        # Test whether _move correctly updates the position for Direction.DOWN

        # Set the initial position of the snake head
        self.game.head = Point(0, 0)

        # Call the _move method with Direction.DOWN
        self.game._move(Direction.DOWN)

        # Check that the head is moved down by BLOCK_SIZE
        self.assertEqual(self.game.head, Point(0, BLOCK_SIZE))

    def test_move_up(self):
        # Test whether _move correctly updates the position for Direction.UP

        # Set the initial position of the snake head
        self.game.head = Point(0, BLOCK_SIZE)

        # Call the _move method with Direction.UP
        self.game._move(Direction.UP)

        # Check that the head is moved up by BLOCK_SIZE
        self.assertEqual(self.game.head, Point(0, 0))


if __name__ == '__main__':
 unittest.main()


        
        
