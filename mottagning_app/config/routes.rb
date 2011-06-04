MottagningApp::Application.routes.draw do

  ActiveAdmin.routes(self)

  match 'page/:id', :controller => :pages, :action => :show
  
end
