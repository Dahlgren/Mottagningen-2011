class FixFadder < ActiveRecord::Migration
  def self.up
    change_table :fadders do |t|
      t.remove :fb_id
      t.string :facebookid
    end
  end

  def self.down
    change_table :fadders do |t|
      t.remove :facebookid
      t.string :fb_id
    end
  end
end
