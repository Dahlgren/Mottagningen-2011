ActiveAdmin.register Page do
  index do
      column :id
      column "Title" do |page| 
        link_to page.title, admin_page_path(page)
      end
      column :url
      column :created_at
      column :updated_at
      default_actions
    end
  
  form do |f|
    f.inputs "Details" do
      f.input :title
    end
    f.inputs "Content" do
      f.input :content
    end
    f.buttons
  end
  
  filter :title
  filter :url
end
