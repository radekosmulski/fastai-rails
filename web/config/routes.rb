Rails.application.routes.draw do
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
  root to: 'images#upload'
  post 'show_results', to: 'images#show_results'
end
