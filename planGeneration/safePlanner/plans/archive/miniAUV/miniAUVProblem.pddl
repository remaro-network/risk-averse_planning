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
