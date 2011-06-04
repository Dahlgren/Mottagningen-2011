class CreateFadders < ActiveRecord::Migration
  def self.up
    create_table :fadders do |t|
      t.string :name
      t.string :fb_id
      t.timestamps
    end
  end

  def self.down
    drop_table :fadders
  end
end
