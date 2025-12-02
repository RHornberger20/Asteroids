import pygame
import sys
from constants import *
from player import *
from logger import log_state, log_event
from asteroid import *
from asteroidfield import *

def main():

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	Player.containers = (updatable, drawable)
	AsteroidField.containers = (updatable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroidfield = AsteroidField()

	pygame.init()

	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



	while True:
		log_state()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updatable.update(dt)

		for obj in asteroids:
			if obj.collides_with(player):
				log_event("player_hit")
				print("Game over!")
				sys.exit()

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60)/1000


	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()
