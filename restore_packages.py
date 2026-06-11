from app import app, db
from app import Shipment
from datetime import datetime

with app.app_context():
    
    # PACKAGE 1: Incoming Package from UK
    package1 = Shipment(
        tracking_code="INT-UK-2026-479432",
        shipment_direction="incoming",
        customer_name="Mr. Chris",
        customer_email=None,
        customer_phone="+447570149032",
        origin="United Kingdom",
        destination="Lagos",
        package_type="Parcel",
        package_weight=24.0,
        status="In transit to Lagos",
        current_location="Currently in Transit",
        estimated_delivery="2026-06-11",
        last_update=datetime(2026, 6, 4, 19, 53, 0),
        origin_country="UK",
        partner_courier_original="Royal Mail",
        is_local=False,
        delivery_type="standard"
    )
    db.session.add(package1)
    print("✅ Package 1 (INT-UK-2026-479432) added successfully!")
    
    # PACKAGE 2: Outgoing Package to UK
    package2 = Shipment(
        tracking_code="DJL-2026-HXESB",
        shipment_direction="outgoing",
        customer_name="Areo Tolulope B",
        customer_email="toluare123@gmail.com",
        customer_phone="+447833889142",
        origin="Ibadan",
        destination="Wolverhampton, United Kingdom",
        package_type="Parcel",
        package_weight=10.0,
        status="Arrived at Lagos Airport",
        current_location="Lagos Hub",
        estimated_delivery="June 10, 2026",
        last_update=datetime(2026, 6, 4, 12, 56, 0),
        partner_courier="FedEx",
        is_local=False,
        delivery_type="standard"
    )
    db.session.add(package2)
    print("✅ Package 2 (DJL-2026-HXESB) added successfully!")
    
    # SAVE TO DATABASE
    db.session.commit()
    print("-" * 50)
    print("🎉 BOTH PACKAGES RESTORED SUCCESSFULLY!")
    print("-" * 50)
    
    # Verify
    count = Shipment.query.count()
    print(f"Total shipments in database: {count}")