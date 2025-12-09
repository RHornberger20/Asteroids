from circleshape import *
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x,y, radius)


	def draw(self, screen):
		pygame.draw.circle(screen, (255,255,255), self.position, self.radius, LINE_WIDTH)

	def update(self,dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if (self.radius <= ASTEROID_MIN_RADIUS):
			return "Nothing"
		else:
			log_event("asteroid_split")
			angle = random.uniform(20,50)
			pa_velocity = self.velocity.rotate(angle)
			na_velocity = self.velocity.rotate(-angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS

			asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

			asteroid_1.velocity = pa_velocity * 1.2
			asteroid_2.velocity = na_velocity * 1.2
