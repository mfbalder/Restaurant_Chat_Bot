import model
import csv
from datetime import datetime

def load_users(session):
	# yelping_since,compliments.plain,compliments.more,elite,compliments.cute,compliments.writer,fans,compliments.note,type,compliments.hot,compliments.cool,compliments.profile,average_stars,review_count,friends,name,user_id,votes.cool,compliments.list,votes.funny,compliments.photos,compliments.funny,votes.useful

	# f = open("seed_data/users_data.csv")
	# for line in f:
	# 	user_data = line.strip().split(",")

	# 	name, average_rating, user_id = user_data[1], user_data[5], users_data[6]
	# 	new_user = model.User(id=user_id, average_rating=average_rating, name=name)

	# 	session.add(new_user)

	# f.close()

	f = open("seed_data/yelp_academic_dataset_user.csv")
	for line in f:
		user_data = line.strip().split(",")

		name, average_rating, user_id = 
			user_data[15], user_data[12], users_data[16]
		new_user = model.User(id=user_id, average_rating=average_rating, name=name)

		session.add(new_user)

	f.close()



	session.commit()


def load_businesses(session):
	# f = open("seed_data/businesses_data.csv")
	# for line in f:
	# 	business_data = line.strip().split(",")

	# 	business_id, address, categories, city, name, longitude, state, stars, latitude =
	# 		business_data[0], business_data[1], businesses_data[4], business_data[6],
	# 		business_data[7], business_data[9], business_data[10], business_data[11], business_data[12]

	# 	if "Food" not in categories and "Restaurants" not in categories:
	# 		continue

	# 	new_business = model.Restaurant(id=business_id,
	# 									address=address,
	# 									categories=categories,
	# 									city=city,
	# 									name=name,
	# 									longitude=longitude,
	# 									latitude=latitude,
	# 									state=state,
	# 									stars=stars)

	# 	session.add(new_business)

	# f.close()
	# attributes.Ambience.divey,attributes.Dietary Restrictions.vegan,attributes.Happy Hour,hours.Thursday.open,attributes.Order at Counter,attributes.Hair Types Specialized In.africanamerican,6attributes.Hair Types Specialized In.kids,7attributes.BYOB,hours.Friday.open,8categories,9latitude,10attributes.Outdoor Seating,11attributes.Alcohol,12attributes.Ambience.classy,13attributes.Payment Types.mastercard,14attributes.Parking.lot,15business_id,16attributes.Ambience.touristy,17attributes.Corkage,18hours.Tuesday.open,19attributes.Good For.brunch,20attributes.Payment Types.amex,21name,22hours.Monday.open,23attributes.Waiter Service,24attributes.Parking.street,25attributes.Ambience.hipster,26attributes.BYOB/Corkage,27attributes.Hair Types Specialized In.straightperms,28attributes.Music.live,29attributes.Dietary Restrictions.dairy-free,30attributes.Music.background_music,31attributes.Price Range,32attributes.Good For.breakfast,33attributes.Parking.garage,34attributes.Music.karaoke,35attributes.Good For Dancing,36review_count,37attributes.Hair Types Specialized In.asian,38state,39attributes.Accepts Credit Cards,40hours.Friday.close,41attributes.Good For.lunch,42attributes.Good For Kids,43attributes.Parking.valet,44attributes.Take-out,45full_address,46hours.Thursday.close,47attributes.Hair Types Specialized In.coloring,48attributes.Payment Types.cash_only,49attributes.Good For.dessert,50attributes.Music.video,51attributes.Dietary Restrictions.halal,52attributes.Takes Reservations,53hours.Saturday.open,54attributes.Ages Allowed,55attributes.Ambience.trendy,56attributes.Delivery,57hours.Wednesday.close,58attributes.Wi-Fi,59open,60city,61attributes.Payment Types.discover,62attributes.Wheelchair Accessible,63attributes.Dietary Restrictions.gluten-free,64stars,65attributes.Payment Types.visa,66type,67attributes.Caters,68attributes.Ambience.intimate,69attributes.Music.playlist,70attributes.Good For.latenight,71attributes.Good For.dinner,72attributes.Coat Check,73longitude,74hours.Monday.close,75attributes.Hair Types Specialized In.extensions,76hours.Tuesday.close,77hours.Saturday.close,78attributes.Good for Kids,79attributes.Parking.validated,80hours.Sunday.open,81attributes.Accepts Insurance,82attributes.Music.dj,83attributes.Dietary Restrictions.soy-free,84attributes.Has TV,85hours.Sunday.close,86attributes.Ambience.casual,87attributes.By Appointment Only,88attributes.Dietary Restrictions.kosher,89attributes.Dogs Allowed,90attributes.Drive-Thru,91attributes.Dietary Restrictions.vegetarian,92hours.Wednesday.open,93attributes.Noise Level,94attributes.Smoking,95attributes.Attire,96attributes.Hair Types Specialized In.curly,97attributes.Good For Groups,98neighborhoods,99attributes.Open 24 Hours,100attributes.Ambience.romantic,101attributes.Hair Types Specialized In.perms,102attributes.Music.jukebox,103attributes.Ambience.upscale

	f = open("seed_data/yelp_academic_dataset_business.csv")
	for line in f:
		bus_data = line.strip().split(",")
		divey = bus_data[0]
		vegan = bus_data[1]
		happy_hour = bus_data[2]
		open_thurs = bus_data[3]
		counter = bus_data[4]
		byob = bus_data[7]
		open_fri = bus_data[8]
		categories = bus_data[9]
		latitude = bus_data[10]
		outdoor_seating = bus_data[11]
		alcohol = bus_data[12]
		classy = bus_data[13]
		mastercard = bus_data[14]
		parking_lot = bus_data[15]
		business_id = bus_data[16]
		touristy = bus_data[17]
		corkage = bus_data[18]
		open_tues = bus_data[19]
		brunch = bus_data[20]
		amex = bus_data[21]
		name = bus_data[22]
		open_mon = bus_data[23]
		waiter = bus_data[24]
		parking_street = bus_data[25]
		hipster = bus_data[26]
		live_music = bus_data[29]
		dairy_free = bus_data[30]
		background_music = bus_data[31]
		price_range = bus_data[32]
		breakfast = bus_data[33]
		parking_garage = bus_data[34]
		state = bus_data[39]
		credit_cards = bus_data[40]
		close_fri = bus_data[41]
		lunch = bus_data[42]
		kids = bus_data[43]
		parking_valet = bus_data[44]
		takeout = bus_data[45]
		address = bus_data[46]
		close_thurs = bus_data[47]
		cash_only = bus_data[49]
		dessert = bus_data[50]
		halal = bus_data[52]
		reservations = bus_data[53]
		open_sat = bus_data[54]
		trendy = bus_data[56]
		delivery = bus_data[57]
		close_wed = bus_data[58]
		wifi = bus_data[59]
		is_open = bus_data[60]
		city = bus_data[61]
		discover = bus_data[62]
		wheelchair = bus_data[63]
		gluten_free = bus_data[64]
		stars = bus_data[65]
		visa = bus_data[66]
		intimate = bus_data[69]
		latenight = bus_data[71]
		dinner = bus_data[72]
		coat_check = bus_data[73]
		longitude = bus_data[74]
		close_mon = bus_data[75]
		close_tues = bus_data[77]
		close_sat = bus_data[78]
		open_sun = bus_data[81]
		soy_free = bus_data[84]
		close_sun = bus_data[86]
		casual = bus_data[87]
		kosher = bus_data[89]
		drive_thru = bus_data[91]
		vegetarian = bus_data[92]
		open_wed = bus_data[93]
		noise_level = bus_data[94]
		groups = bus_data[98]
		neighborhoods = bus_data[99]
		twenty_four = bus_data[100]
		romantic = bus_data[101]
		upscale = bus_data[104]

		# check to make sure the business is food related
		if "Food" not in categories and "Restaurants" not in cateogies:
			continue
		# check to make sure only open businesses are added to the database
		if is_open == "FALSE":
			continue

		# turn all open and close times to datetime objects
		def parse_time(t):
			t = datetime.strptime(t, "%H:%M")
			return t

		open_mon = parse_time(open_mon)
		close_mon = parse_time(close_mon)
		open_tues = parse_time(open_tues)
		close_tues = parse_time(close_tues)
		open_wed = parse_time(open_wed)
		close_wed = parse_time(close_wed)
		open_thurs = parse_time(open_thurs)
		close_thurs = parse_time(close_thurs)
		open_fri = parse_time(open_fri)
		close_fri = parse_time(close_fri)
		open_sat = parse_time(open_sat)
		close_sat = parse_time(close_sat)
		open_sun = parse_time(open_sun)
		close_sun = parse_time(close_sun)

		# create a Restaurant object out of the business
		new_business = model.Restaurant(id=business_id, name = name, divey = divey, vegan = vegan,
										happy_hour = happy_hour, open_thurs = open_thurs,
										counter = counter, byob = byob, open_fri = open_fri,
										categories = categories, latitude = latitude, 
										outdoor_seating = outdoor_seating, alcohol = alcohol,
										classy = classy, mastercard = mastercard, parking_lot = parking_lot,
										touristy = touristy, corkage = corkage, open_tues = open_tues,
										brunch = brunch, amex = amex, open_mon = open_mon, waiter = waiter,
										parking_street = parking_street, hipster = hipster,
										live_music = live_music, dairy_free = dairy_free,
										background_music = background_music, price_range = price_range,
										breakfast = breakfast, parking_garage = parking_garage,
										state = state, credit_cards = credit_cards, close_fri = close_fri,
										lunch = lunch, kids = kids, parking_valet = parking_valet,
										takeout = takeout, address = address, close_thurs = close_thurs,
										cash_only = cash_only, dessert = dessert, halal = halal,
										reservations = reservations, open_sat = open_sat, trendy = trendy,
										delivery = delivery, close_wed = close_wed, wifi = wifi,
										city = city, discover = discover, wheelchair = wheelchair,
										gluten_free = gluten_free, stars = stars, visa = visa, intimate = intimate,
										latenight = latenight, dinner = dinner, coat_check = coat_check,
										longitude = longitude, close_mon = close_mon, close_tues = close_tues,
										close_sat = close_sat, open_sun = open_sun, soy_free = soy_free,
										close_sun = close_sun, casual = casual, kosher = kosher,
										drive_thru = drive_thru, vegetarian = vegetarian, open_wed = open_wed,
										noise_level = noise_level, groups = groups, neighborhoods = neighborhoods,
										twenty_four = twenty_four, romantic = romantic, upscale = upscale)

		session.add(new_business)

		f.close()

	session.commit()

																								


def load_ratings(session):
	# f = open("seed_data/ratings_data.csv")
	# for line in f:
	# 	rating_data = line.strip().split(",")

	# 	user_id, review_id, text, business_id, stars = rating_data[0], rating_data[1], rating_data[2],
	# 		rating_data[4], rating_data[6]
				
	# 	new_rating = model.Rating(id=review_id,
	# 							  user_id=user_id,
	# 							  business_id=business_id,
	# 							  review_text=text,
	# 							  stars=stars)

	# 	session.add(new_rating)

	# f.close()

	# user_id,review_id,text,votes.cool,business_id,votes.funny,stars,date,type,votes.useful
	f = open("seed_data/yelp_academic_dataset_review.csv")
	for line in f:
		rating_data = line.strip().split(",")
		user_id, review_id, text, business_id, stars, useful_votes = 
			rating_data[0], rating_data[1], rating_data[2], rating_data[4], rating_data[6], rating_data[9]

		new_rating = model.Rating(id=review_id,
								  user_id=user_id,
								  business_id=business_id,
								  review_text=text,
								  stars=stars,
								  useful_votes=useful_votes)

		session.add(new_rating)

	f.close()


	session.commit()


	def main(session):
		load_users(session)
		load_businesses(session)
		load_ratings(session)

	if __name__ == "__main__":
		s = model.connect()
		main(s)
		







