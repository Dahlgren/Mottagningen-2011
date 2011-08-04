MottagningApp::Application.routes.draw do

  ActiveAdmin.routes(self)
  
  root :to => "days#index"
  
  match 'people', :controller => :people, :action => :show

  match 'page/:id', :controller => :pages, :action => :show
  
  match 'timeedit/events', :controller => :timeedit, :action => :list
  
end
