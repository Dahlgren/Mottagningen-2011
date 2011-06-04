ActiveAdmin.register Fadder do
  index do
      column :id
      column :name
      column "Facebook ID", :facebookid 
      default_actions
    end
  
  form do |f|
    f.inputs "Details" do
      f.input :name
      f.input :facebookid, :label => "Facebook ID"
    end
    f.buttons
  end
  
  filter :name
  filter :facebookid
end
