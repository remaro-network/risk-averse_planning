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
        )
        :effect (and 
            (probabilistic 
                ; 50% chance to get a good photo
                0.5 (hasPhoto ?wp)
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
                0.9 (when (dangerousForCamera ?from ?to) (brokenCamera ?camera))
            )
            (probabilistic
                0.9 (when (dangerousForThruster ?from ?to) (brokenThruster ?thruster))
            )
            
        )
    )
)

(define (problem navigationMiniAUV)
    (:domain miniAUV)
    (:objects
        auv - robot
        rgbCamera - camera
        backThruster - thruster
        startPoint - waypoint
        endPoint - waypoint
        photoPoint - waypoint
    )

    (:init
        (at auv startPoint)
        (dangerousForCamera startPoint photoPoint)
        (dangerousForThruster photoPoint endPoint)
    )

    (:goal
        (at auv endPoint)
        (hasPhoto photoPoint)
    )
)
