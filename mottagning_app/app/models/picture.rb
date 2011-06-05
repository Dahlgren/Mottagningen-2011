class Picture < ActiveRecord::Base
  IMAGE_ANDROID_WIDTH = "x480"
  IMAGE_FEED = "590x700>"
  IMAGE_THUMB_WIDTH = "x240"
  IMAGE_COLLAGE_LARGE = "360x360#"
  IMAGE_COLLAGE_THUMB = "120x120#"
  IMAGE_LARGE_FEED =  "1000x1000>"
  
  has_attached_file :image,
    :styles => { :feed => IMAGE_FEED, :android => IMAGE_ANDROID_WIDTH, :thumb => IMAGE_THUMB_WIDTH, :collage_thumb => IMAGE_COLLAGE_THUMB, :collage_large => IMAGE_COLLAGE_LARGE, :large_feed => IMAGE_LARGE_FEED},
    :dependent => :destroy,
    :url => "/system/:attachment/:id/:style/:normalized_filename",
    :path => ":rails_root/public/system/:attachment/:id/:style/:normalized_filename"

  Paperclip.interpolates :normalized_filename do |attachment, style|
    attachment.instance.normalized_filename
  end

  def normalized_filename
    "#{self.id}-#{self.image_file_name.gsub( /[^a-zA-Z0-9_\.]/, '')}"
  end
  
  has_many :comments, :dependent => :destroy
  has_many :reports, :dependent => :destroy
  belongs_to :day
  
  validates :image_file_name, :presence => true
  validates :comment, :presence => true, :length => {:minimum => 3, :maximum => 500}
  validates_attachment_size :image, :less_than => 10.megabytes
  
  validate :allowed_content_types?
  validate :not_only_spaces 
      
  attr_accessible :image, :comment
  
  validate :image_size
  validate :user_exist
  
  IMAGE_MINIMUM_SIZE = [300, 300]
  IMAGE_MAXIMUM_SIZE = [5000, 5000]
  

  def fix_url(relative_path, url)
    url = url.split("/")
    url_return = url[0] + '//' + url[2] + relative_path
    url_return
  end 
  
  private
  
  def allowed_content_types?
     unless ["image/jpeg", "image/png", "image/gif", "application/octet-stream"].include?(self.image_content_type)
      errors.add(:image_content_type, "Not allowed!")
    end
  end
    
  def not_only_spaces
    if self.comment.gsub(/[ ]/, '').empty?
      errors.add(:comment, "Plz type something")
    end
  end
  
  def image_size
    begin
        temp_file = image.queued_for_write[:original] #get the file that is being uploaded
      unless temp_file == nil
        dimensions = Paperclip::Geometry.from_file(temp_file)
        unless (dimensions.width >= IMAGE_MINIMUM_SIZE[1]) && (dimensions.height >= IMAGE_MINIMUM_SIZE[0])
          errors.add( :image, "to small! Minumum size #{IMAGE_MINIMUM_SIZE[1]}x#{IMAGE_MINIMUM_SIZE[0]}px.")
        end
        unless (dimensions.width <= IMAGE_MAXIMUM_SIZE[1]) && (dimensions.height <= IMAGE_MAXIMUM_SIZE[0])
          errors.add( :image, "to big! Maximum size #{IMAGE_MAXIMUM_SIZE[1]}x#{IMAGE_MAXIMUM_SIZE[0]}px.")
        end
        ratio = (dimensions.width / dimensions.height)
        unless (ratio >= 0.1) && (ratio <= 5)
          errors.add(:image, "has an invalid aspect ratio! The width:height ratio should be inbetween 1:10 and 5:1!")
        end
      end 
    end
    rescue Exception => e
  end
end
