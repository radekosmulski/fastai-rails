## fastai-rails - a docker setup for serving a deep learning model with a front-end component

Steps to get up and running:
1. Install docker and docker-compose
2. Clone repository and cd into it
3. Run `docker-compose up` and wait for the images to be built
4. Navigate to `localhost` in your browser

The frontend is a [rails](https://rubyonrails.org/) application. The API endpoint runs on [starlette](https://www.starlette.io/).

This is a minimal setup created for demonstration purposes. The files of interest are:
- [upload.html.erb](https://github.com/radekosmulski/fastai-rails/blob/master/web/app/views/images/upload.html.erb) - image upload form rendered when navigating to `localhost`
- [images_controller.rb](https://github.com/radekosmulski/fastai-rails/blob/master/web/app/controllers/images_controller.rb) - rails controller handling the logic of reaching out to the API endpoint
- [api.py](https://github.com/radekosmulski/fastai-rails/blob/master/api/api.py) - entire starlette app for the API endpoint
- [show_results.html.erb](https://github.com/radekosmulski/fastai-rails/blob/master/web/app/views/images/show_results.html.erb) - template file for rendering the results to the user
- [pets.ipynb](https://github.com/radekosmulski/fastai-rails/blob/master/train/pets.ipynb) - a jupyter notebook for training and saving the model


I recorded a [walkthrough](https://youtu.be/BeJ80peD3Qs) where I follow a request starting with a user uploading an image to displaying the results.
