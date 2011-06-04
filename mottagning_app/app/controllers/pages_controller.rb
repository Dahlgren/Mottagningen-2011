class PagesController < ApplicationController
  def show
    @page = Page.where(:id => params[:url]).first
  end
end
