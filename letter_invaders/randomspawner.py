
import random
from fallingletters import *

class RandomSpawner:

    def __init__(self, letters, width, height, danger_bar):
        self.letters = letters
        self.screen_width = width
        self.screen_height = height
        self.danger_bar = danger_bar

        self.falling_letters = []
        self.missing_letters = []

        # Difficulty settings
        self.game_time = 0.0
        self.difficulty_interval = 10.0
        self.difficulty_level = 0

        self.spawn_interval = 2.5
        self.spawn_timer = 0.0
        self.fall_speed = 40

        # Spawn the first letter immediately
        self.spawn()

    def spawn(self):
        x = random.randint(20, self.screen_width - 20)

        letter = FallingLetters(
            self.letters,
            x,
            0,
            self.screen_height,
            self.fall_speed
        )

        print("Spawned letter:", letter.letters)
        self.falling_letters.append(letter)

    def update(self, dt):
        self.game_time += dt

        # Increase difficulty every 10 seconds
        new_level = int(self.game_time // self.difficulty_interval)

        if new_level > self.difficulty_level:
            self.difficulty_level = new_level

            # Spawn more frequently, but never faster than every 0.5 sec
            self.spawn_interval = max(
                0.5, 2.5 - self.difficulty_level * 0.2
            )

            # Increase falling speed gradually
            self.fall_speed = min(
                150, 40 + self.difficulty_level * 10
            )

        # Spawn letters according to the current interval
        self.spawn_timer += dt

        if self.spawn_timer >= self.spawn_interval:
            self.spawn()
            self.spawn_timer -= self.spawn_interval

        # Update existing letters
        for letter in self.falling_letters[:]:
            letter.update(dt)

            if letter.selected:
                self.falling_letters.remove(letter)

            elif letter.reachBottom():
                self.danger_bar.hit(letter.x)
                self.falling_letters.remove(letter)
                self.missing_letters.append(letter)

    def draw(self, surface):
        for letter in self.falling_letters:
            letter.draw(surface)