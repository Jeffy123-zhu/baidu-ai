"""
Demo script showcasing MediDoc AI capabilities
Simulates the three main scenarios
"""

from loguru import logger
import time


def demo_scenario_1_emergency():
    """Scenario 1: Emergency Fast Registration"""
    print("\n" + "="*60)
    print("SCENARIO 1: Emergency Fast Registration")
    print("="*60)
    print("\nPatient arrives at ER with paper medical records...")
    time.sleep(1)
    
    print("\n[Step 1] Placing document under scanner...")
    time.sleep(0.5)
    
    print("[Step 2] Running OCR recognition... (0.8s)")
    time.sleep(0.8)
    print("  ✓ Text extracted with 96% confidence")
    
    print("[Step 3] Auto-structuring data... (0.3s)")
    time.sleep(0.3)
    print("  ✓ Patient info: Male, 65 years old")
    print("  ✓ Chief complaint: Chest discomfort")
    
    print("[Step 4] AI preliminary analysis... (0.9s)")
    time.sleep(0.9)
    print("  ✓ Flagged for cardiology review")
    
    print("\n✅ Total time: 2.0s (vs traditional 5 minutes)")


def demo_scenario_2_consultation():
    """Scenario 2: Multi-disciplinary Consultation"""
    print("\n" + "="*60)
    print("SCENARIO 2: Multi-Disciplinary Consultation")
    print("="*60)
    print("\nComplex case: 65yo male, chest pain, abnormal ECG...")
    time.sleep(1)
    
    print("\n[Step 1] Uploading examination data...")
    time.sleep(0.5)
    print("  ✓ ECG uploaded")
    print("  ✓ Blood test results uploaded")
    print("  ✓ CT scan report uploaded")
    
    print("\n[Step 2] Multi-agent analysis in progress...")
    print("  🤖 Cardiology Agent analyzing...")
    time.sleep(2)
    print("     → Possible coronary artery disease")
    print("     → Recommend coronary angiography")
    
    print("  🤖 Radiology Agent analyzing...")
    time.sleep(2)
    print("     → Left ventricular hypertrophy detected")
    print("     → Aortic calcification present")
    
    print("  🤖 Medication Agent analyzing...")
    time.sleep(1)
    print("     → Recommend: Aspirin + Statin")
    print("     → Monitor liver function")
    
    print("\n[Step 3] Agent debate for consensus...")
    time.sleep(2)
    print("  ✓ Consensus reached (94% agreement)")
    
    print("\n[Step 4] Generating reports...")
    time.sleep(1)
    print("  ✓ Professional report generated")
    print("  ✓ Patient-friendly report generated")
    
    print("\n✅ Total time: 25s (vs traditional 2-3 days)")


def demo_scenario_3_offline():
    """Scenario 3: Remote Rural Healthcare"""
    print("\n" + "="*60)
    print("SCENARIO 3: Remote Rural Healthcare (Offline)")
    print("="*60)
    print("\nRural clinic with no internet connection...")
    time.sleep(1)
    
    print("\n[Status] Edge device in OFFLINE mode")
    print("[Status] Using local quantized models")
    
    print("\n[Step 1] Scanning patient history...")
    time.sleep(1)
    print("  ✓ Paper records digitized")
    
    print("\n[Step 2] Local AI analysis...")
    time.sleep(2)
    print("  ✓ Medical history extracted")
    print("  ✓ Preliminary diagnosis: Hypertension")
    print("  ✓ Recommendations generated")
    
    print("\n[Step 3] Storing for later sync...")
    print("  ✓ Case saved to local cache")
    
    print("\n[Network Restored]")
    time.sleep(1)
    print("[Step 4] Auto-syncing to cloud...")
    time.sleep(1)
    print("  ✓ 1 case uploaded")
    print("  ✓ Cloud analysis complete")
    print("  ✓ Updated recommendations pushed to device")
    
    print("\n✅ Offline capability: 100% functional")


def main():
    """Run all demo scenarios"""
    print("\n" + "🏥"*30)
    print("MediDoc AI - System Demonstration")
    print("🏥"*30)
    
    try:
        demo_scenario_1_emergency()
        input("\nPress Enter to continue to Scenario 2...")
        
        demo_scenario_2_consultation()
        input("\nPress Enter to continue to Scenario 3...")
        
        demo_scenario_3_offline()
        
        print("\n" + "="*60)
        print("Demo Complete!")
        print("="*60)
        print("\nKey Achievements:")
        print("  • 10x faster document processing")
        print("  • Multi-agent collaborative diagnosis")
        print("  • 100% offline capability")
        print("  • Edge-cloud hybrid deployment")
        
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user")


if __name__ == "__main__":
    main()
