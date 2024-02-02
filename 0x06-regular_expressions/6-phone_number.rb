#!/usr/bin/env ruby
# Regexp that matches a 10 digit phone number

puts ARGV[0].scan(/\b\d{10}\b/).join
