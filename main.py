import pygame
import sys
from constants import *
from player import *
from logger import log_state, log_event
from asteroid import *
from asteroidfield import *
from shot import *


def main():


	pygame.mixer.pre_init(44100, -16, 1, 4096)
	pygame.init()

	pygame.mixer.music.load('Asteroids_All_Around_Us.ogg')
	# Loops indefinitely
	pygame.mixer.music.play(loops=-1)

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable,drawable)
	Player.containers = (updatable, drawable)
	AsteroidField.containers = (updatable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroidfield = AsteroidField()

	#initalize dt and score
	dt = 0
	score = 0

	while True:
		log_state()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return


		font = pygame.font.Font(None,36)

		updatable.update(dt)

		screen.fill("black")

		score_text = font.render(f'Score: {score}', True, (255,255,255))
		screen.blit(score_text, (10,10))

		for asteroid in asteroids:
			if asteroid.collides_with(player):
				log_event("player_hit")
				print("Game over!")
				print(f"Final Score: {score}")
				sys.exit()
			for shot in shots:
				if asteroid.collides_with(shot):
					log_event("asteroid_shot")
					asteroid.kill()
					shot.kill()
					if asteroid.split() == "Nothing":
						score += 50
					else:
						score += 100
					screen.blit(score_text, (10,10))

		for obj in drawable:
			obj.draw(screen)

		if score >= 1000:
			player.color_change_green(screen)
		if score >= 5000:
			player.color_change_red(screen)
		if score > 10000:
			player.color_change_purple(screen)

		pygame.display.flip()

		dt = clock.tick(60)/1000


	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()
