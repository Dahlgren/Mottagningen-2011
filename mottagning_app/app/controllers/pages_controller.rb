class PagesController < ApplicationController
  def show
    @page = Page.where(:url => params[:id]).first
  end
end
