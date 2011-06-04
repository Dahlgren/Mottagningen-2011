MottagningApp::Application.routes.draw do
  ActiveAdmin.routes(self)

  
  match 'page/:url', :controller => :pages, :action => :show
end
