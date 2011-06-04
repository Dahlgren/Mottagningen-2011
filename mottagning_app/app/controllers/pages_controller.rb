class PagesController < ApplicationController
  def show
    @page = Page.where(:id => params[:id]).first
  end
end
