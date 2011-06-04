class DaysCreateFields < ActiveRecord::Migration
  def self.up
    change_table :days do |t|
      t.date :date
      t.string :title
      t.text :text
    end
  end

  def self.down
    change_table :days do |t|
      t.remove :date
      t.remove :title
      t.remove :text
    end
  end
end
