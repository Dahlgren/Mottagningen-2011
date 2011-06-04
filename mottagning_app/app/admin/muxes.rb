ActiveAdmin.register Mux do
  index do
      column :id
      column :name
      column :title
      column "Facebook ID", :facebookid
      column :rank
      default_actions
    end
  
  form do |f|
    f.inputs "Details" do
      f.input :name
      f.input :title
      f.input :facebookid, :label => "Facebook ID"
      f.input :rank
    end
    f.buttons
  end
  
  filter :name
  filter :facebookid
end
