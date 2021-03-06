def site_settings_processor(request):
	context_dictionary = {
		# 'root_url': 'jpark.pythonanywhere.com',
		'root_url': '127.0.0.1:8000',
		'admin_name': 'super',
		'company_name': 'Spray Pros',
		'footer_copyright': 'Spray Pros, 2014',
		'logo_file_name': 'images/logo_big.png',
		'site_email': 'jaredjamespark@gmail.com',
		'meta_content': 'A template website design geared toward pest control services',
		'meta_keywords': 'pest control, termites, scorpions, bedbugs, bed bugs',
		# 'first_name': 'David',
		'navbar_link1_name': 'about',
		'navbar_link1_text': 'Informational',
		'navbar_link2_name': 'products',
		'navbar_link2_text': 'Revenue Generating',
		'navbar_link3_name': 'contact',
		'navbar_link3_text': 'Contact',
		'call_to_action_button_text': 'Contact us today',
		'call_to_action_text': "to learn the 5 things your pest guy isn't telling you.",
		'main_image_file': 'images/fly_flick_crop.jpg',
		'main_image_header_text': 'Your service or promotion',
		'main_image_content_text': 'Text to motivate action',
		'main_image_button_text': 'Learn More',
		'main_image_button_link_name': 'products',
		'homepage_content_top': 'This space can contain a brief introduction to the company. Another alternative is to include some user feedback',
		'homepage_content_quote': '"You could put a customer\'s quote right here for everyone to see"',
		 'homepage_content_quote_name': 'John D',
		'img1_file': 'images/termite.jpg',
		'img1_alt': 'Wood eaters',
		'img1_title': 'wood monsters',
		'img1_text': "This is where text goes for the first image. This entire area links to one of your pages.",
		'img1_link_name': 'products',
		'img2_file': 'images/scorpion.jpg',
		'img2_alt': 'tiny tanks',
		'img2_title': 'Scorpions',
		'img2_text': "This is where text goes for the second image. This entire area links to one of your pages.",
		'img2_link_name': 'products',
		'img3_file': 'images/bed_bug.jpg',
		'img3_alt': 'creepy',
		'img3_title': 'Bed Bugs',
		'img3_text': "This is where text goes for the third image. This entire area links to one of your pages.",
		'img3_link_name': 'specials',
		'left_sidebar_img_file': 'images/awful_sidebar.png',
		'default_testimonial': 'For now this is one quote that you can feature at the bottom of every non-homepage page. The goal is for this space to randomly cycle through a list of quotes, reloaded for each new page request.',
		'default_unique_content_title': 'Unique Website Content',
		'default_unique_content_text': 'This area can link to some unique content that adds to the visitor experience. Ask us about some of our popular options for your industry (kids section, monthly promotions, free information/sampler product, twitter feed, rss feed, etc)',
	}
	return(context_dictionary)