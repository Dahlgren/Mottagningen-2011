ActiveAdmin.register Day do
  index do
      column :id
      column :date
      column :title
      default_actions
    end
  
  form do |f|
    f.inputs "Details" do
      f.input :title
      f.input :date
      f.input :text
    end
    f.buttons
  end
  
  filter :title
  filter :date
end
