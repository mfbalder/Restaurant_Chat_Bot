from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session


# ENGINE = None
# Session = None

# def connect():
# 	global ENGINE
# 	global Session

# 	ENGINE = create_engine("postgresql://localhost/restaurantrec", echo=False)
# 	Session = sessionmaker(bind=ENGINE)

# 	return Session()
	
# session = connect()

# Base = declarative_base()

ENGINE = create_engine("postgresql://localhost/restaurantrec", echo=False)
session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

class User(Base):
	__tablename__ = "users"

	id = Column(String(100), primary_key = True)
	email = Column(String(64), nullable = True)
	password = Column(String(64), nullable = True)
	name = Column(String(64), nullable = True)
	average_rating = Column(Float, nullable = True)


class Restaurant(Base):
	__tablename__ = "restaurants"

	id = Column(String(120), primary_key = True)
	name = Column(String(120), nullable = False)
	divey = Column(Boolean, nullable = True)
	vegan = Column(Boolean, nullable = True)
	happy_hour = Column(Boolean, nullable = True)
	open_thurs = Column(DateTime, nullable = True)
	counter = Column(Boolean, nullable = True)
	byob = Column(Boolean, nullable = True)
	open_fri = Column(DateTime, nullable = True)
	latitude = Column(Float, nullable=True)
	outdoor_seating = Column(Boolean, nullable = True)
	alcohol = Column(Boolean, nullable = True)
	classy = Column(Boolean, nullable = True)
	mastercard = Column(Boolean, nullable = True)
	parking_lot = Column(Boolean, nullable = True)
	touristy = Column(Boolean, nullable = True)
	corkage = Column(Boolean, nullable = True)
	open_tues = Column(DateTime, nullable = True)
	brunch = Column(Boolean, nullable = True)
	amex = Column(Boolean, nullable = True)
	open_mon = Column(DateTime, nullable = True)
	waiter = Column(Boolean, nullable = True)
	parking_street = Column(Boolean, nullable = True)
	hipster = Column(Boolean, nullable = True)
	live_music = Column(Boolean, nullable = True)
	dairy_free = Column(Boolean, nullable = True)
	background_music = Column(Boolean, nullable = True)
	price_range = Column(Integer, nullable = True)
	breakfast = Column(Boolean, nullable = True)
	parking_garage = Column(Boolean, nullable = True)
	state = Column(String(5), nullable = True)
	credit_cards = Column(Boolean, nullable = True)
	close_fri = Column(DateTime, nullable = True)
	lunch = Column(Boolean, nullable = True)
	kids = Column(Boolean, nullable = True)
	parking_valet = Column(Boolean, nullable = True)
	takeout = Column(Boolean, nullable = True)
	address = Column(String(120), nullable = True)
	close_thurs = Column(DateTime, nullable = True)
	cash_only = Column(Boolean, nullable = True)
	dessert = Column(Boolean, nullable = True)
	halal = Column(Boolean, nullable = True)
	reservations = Column(Boolean, nullable = True)
	open_sat = Column(DateTime, nullable = True)
	trendy = Column(Boolean, nullable = True)
	delivery = Column(Boolean, nullable = True)
	close_wed = Column(DateTime, nullable = True)
	wifi = Column(String(10), nullable = True)
	city = Column(String(64), nullable = True)
	discover = Column(Boolean, nullable = True)
	wheelchair = Column(Boolean, nullable = True)
	gluten_free = Column(Boolean, nullable = True)
	stars = Column(Float, nullable = True)
	visa = Column(Boolean, nullable = True)
	intimate = Column(Boolean, nullable = True)
	latenight = Column(Boolean, nullable = True)
	dinner = Column(Boolean, nullable = True)
	coat_check = Column(Boolean, nullable = True)
	longitude = Column(Float, nullable = True)
	close_mon = Column(DateTime, nullable = True)
	close_tues = Column(DateTime, nullable = True)
	close_sat = Column(DateTime, nullable = True)
	open_sun = Column(DateTime, nullable = True)
	soy_free = Column(Boolean, nullable = True)
	close_sun = Column(DateTime, nullable = True)
	casual = Column(Boolean, nullable = True)
	kosher = Column(Boolean, nullable = True)
	drive_thru = Column(Boolean, nullable = True)
	vegetarian = Column(Boolean, nullable = True)
	open_wed = Column(DateTime, nullable = True)
	noise_level = Column(String(10), nullable = True)
	groups = Column(Boolean, nullable = True)
	twenty_four = Column(Boolean, nullable = True)
	romantic = Column(Boolean, nullable = True)
	upscale = Column(Boolean, nullable = True)

class Rating(Base):
	__tablename__ = "ratings"

	id = Column(String(100), primary_key = True)
	user_id = Column(String(100), ForeignKey("users.id"), nullable = False)
	business_id = Column(String(100), ForeignKey("restaurants.id"), nullable = False)
	review_text = Column(Text, nullable = True)
	stars = Column(Float, nullable = True)
	useful_votes = Column(Float, nullable = True)

	user = relationship("User", backref=backref("ratings", order_by=id))
	restaurant = relationship("Restaurant", backref=backref("restaurants", order_by=id))

class Category(Base):
	__tablename__ = "categories"

	id = Column(Integer, primary_key = True)
	business_id = Column(String(100), ForeignKey("restaurants.id"), nullable = False)
	category = Column(String(100), nullable = False)

	restaurant = relationship("Restaurant", backref=backref("categories"))

class Neighborhood(Base):
	__tablename__ = "neighborhoods"

	id = Column(Integer, primary_key = True)
	business_id = Column(String(100), ForeignKey("restaurants.id"), nullable = False)
	neighborhood = Column(String(100), nullable = False)

	restaurant = relationship("Restaurant", backref=backref("neighborhoods"))

def main():
	pass

if __name__ == "__main__":
	main()
