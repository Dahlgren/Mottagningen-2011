class CreateMuxes < ActiveRecord::Migration
  def self.up
    create_table :muxes do |t|
      t.string :name
      t.string :fb_id
      t.string :title
      t.integer :rank
      t.timestamps
    end
  end

  def self.down
    drop_table :muxes
  end
end
