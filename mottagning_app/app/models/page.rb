class Page < ActiveRecord::Base
  
  validates_presence_of :title
  validates_uniqueness_of :title

  acts_as_url :title
  
  def to_param
    id.to_s + '-' + url
  end

end
