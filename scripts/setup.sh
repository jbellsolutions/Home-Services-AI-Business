#!/bin/bash
# Setup script for Home Services Lead Automation

echo "=== Home Services Lead Automation Setup ==="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 not found. Install it first."
    exit 1
fi

echo "Python: $(python3 --version)"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Install Playwright browsers
echo "Installing Playwright Chromium..."
playwright install chromium

# Create directories
echo "Creating data directories..."
mkdir -p data logs profiles/craigslist profiles/facebook screenshots
mkdir -p craigslist/ad_templates/images/general
mkdir -p craigslist/ad_templates/images/assembly
mkdir -p craigslist/ad_templates/images/painting
mkdir -p craigslist/ad_templates/images/pressure_washing
mkdir -p craigslist/ad_templates/images/drywall
mkdir -p craigslist/ad_templates/images/tv_mounting
mkdir -p craigslist/ad_templates/images/deck_fence

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env from template..."
    cp config/.env.example .env
    echo ""
    echo "IMPORTANT: Edit .env with your credentials before running!"
fi

echo ""
echo "=== Setup Complete ==="
echo ""
echo "Next steps:"
echo "  1. Edit .env with your CL/FB credentials and proxy info"
echo "  2. Add photos to craigslist/ad_templates/images/ folders"
echo "  3. Test proxy: python scripts/test_proxy.py"
echo "  4. Test CL login: python craigslist/poster.py --test"
echo "  5. Test FB login: python facebook/inbox_monitor.py --test"
echo ""
echo "To start automation:"
echo "  CL posting:  python craigslist/poster.py --schedule"
echo "  FB monitor:  python facebook/inbox_monitor.py --monitor"
