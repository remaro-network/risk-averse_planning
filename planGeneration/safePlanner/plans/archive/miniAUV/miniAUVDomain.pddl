(define (domain miniAUV)
    (:requirements :typing :strips :equality :negative-preconditions :conditional-effects :probabilistic-effects  :disjunctive-preconditions) 

    (:types 
        waypoint robot robotPart - object
        camera thruster- robotPart
    )

    (:predicates
        (at ?auv - robot ?wp - waypoint)
        (brokenCamera ?part - camera)
        (brokenThruster ?part - thruster)
        (hasPhoto ?wp - waypoint)
        (dangerousForCamera ?from - waypoint ?to - waypoint)
        (dangerousForThruster ?from - waypoint ?to - waypoint)
    )

    (:action take-photo
        :parameters (
            ?auv - robot
            ?wp - waypoint
            ?camera - camera
        )
        :precondition (and 
            (at ?auv ?wp)
            ;(not (brokenCamera ?camera))
            (not (brokenCamera rgbCamera))
        )
        :effect (and 
            (probabilistic 
                ; 50% chance to get a good photo
                1 (hasPhoto ?wp)
            )
        )
    )

    (:action drive
        :parameters (
            ?auv - robot
            ?from - waypoint
            ?to - waypoint
            ?thruster - thruster
            ?camera - camera
        )
        :precondition (and 
            (at ?auv ?from)
            ;(not (brokenThruster ?thruster))    ; only move if you have a thruster
            (not (brokenThruster backThruster))
        )
        :effect (and 
            (when (not (dangerousForThruster ?from ?to)) (and
                (not (at ?auv ?from))   ; move from first to second waypoint
                (at ?auv ?to)
                )
            )
            ; on dagerous paths, things might break...
            ; TODO: the order of 'probabilistic' and 'when' should ideally be reversed
            (probabilistic 
                0.1 (when (dangerousForCamera ?from ?to) (brokenCamera ?camera))
            )
            (probabilistic
                1 (when (dangerousForThruster ?from ?to) (brokenThruster ?thruster))
            )
            
        )
    )
)
