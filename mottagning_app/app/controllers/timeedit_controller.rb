class TimeeditController < ApplicationController
  
  def list
    require 'net/https'
    require 'ri_cal'
    
    # Mottagningen 2011 id in TimeEdit
    calId = "26973000"
    
    # Make a request to TimeEdit and fetch ical for Mottagningen 2011
    uri = URI.parse('https://schema.sys.kth.se/')
    request = Net::HTTP.new(uri.host, uri.port)
    request.use_ssl = true
    request.verify_mode = OpenSSL::SSL::VERIFY_NONE
    result = request.get("/4DACTION/iCal_downloadReservations/timeedit.ics?id1=#{calId}")
    
    # Parse string and get first calendar
    cal = RiCal.parse_string(result.body.force_encoding("UTF-8")).first
    
    events = {}
    
    # Iterate over events and create a hash with all dates
    cal.events.each do |event|
      if not events.has_key?(event.dtstart.to_date)
        events[event.dtstart.to_date] = []
      end
      
      formatedEvent = {}
      formatedEvent['start'] = event.dtstart.strftime("%H:%M")
      if event.summary != nil
        formatedEvent['title'] = event.summary
      end
      if event.location != nil
        formatedEvent['location'] = event.location
      end
      events[event.dtstart.to_date].push(formatedEvent)
    end
    
    respond_to do |format|
      format.json  { render :json => events }
    end
  end
end