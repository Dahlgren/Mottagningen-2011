class PeopleController < ApplicationController
  def show
    @fadders = Fadder.order('name')
    @muxes = {
      "3" => Mux.order('name').where("rank = 3"),
      "2" => Mux.order('name').where("rank = 2"),
      "1" => Mux.order('name').where("rank = 1")
    }
  end
end
