# ZooOps Product Requirements

## Mission

ZooOps helps high-volume food and beverage operations managers start each day with clarity by centralizing the tools they need to manage daily operations.

## MVP Dashboard

The first version of ZooOps will include:

- Attendance and projected sales
- Schedule layout and call-offs
- Closing manager recap and notes
- Priority-based to-do list
- Important events or unique operational notes

## Primary User

Food and beverage operations managers working in high-volume hospitality environments such as zoos, stadiums, amusement parks, and event venues.

## Problem

Managers often rely on multiple disconnected systems for scheduling, sales, tasks, notes, inventory, events, and communication. This creates unnecessary administrative work and makes it harder to make quick operational decisions.

## Success Criteria

The MVP is successful if a manager can log in and understand the day’s most important operational information within 30 seconds.

## Initial Data Model

### Employee

- id
- first_name
- last_name

### Shift

- id
- employee_id
- location
- in_time
- out_time
- called_off
