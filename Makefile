install_requirements:
	@pip install -r requirements.txt

streamlit:
	streamlit run app.py

heroku_login:
	heroku_login -i

heroku_create_app:
	heroku create mberneaud-taxifare-interface --region eu

deploy_heroku:
	@-git remote add heroku https://git.heroku.com/mberneaud-taxifare-interface.git
	git push heroku master
	heroku ps:scale web=1
