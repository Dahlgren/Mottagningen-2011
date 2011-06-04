class FixMux < ActiveRecord::Migration
  def self.up
    change_table :muxes do |t|
      t.remove :fb_id
      t.string :facebookid
    end
  end

  def self.down
    change_table :muxes do |t|
      t.remove :facebookid
      t.string :fb_id
    end
  end
end
