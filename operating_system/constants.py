"""
L0 — Operating System
Shared constants for the Akshat-AI-System.
All modules import from here. Never hardcode values elsewhere.
"""

# Update Engine Thresholds
PROMOTION_THRESHOLD = 3          # Min independent sources to stage for promotion
RECENT_CHANGES_TTL_DAYS = 90     # Days before review flag triggers
MIN_FREQUENCY_FOR_STAGING = 2   # Min score before appearing as STAGED

# Idea Classification Tags
CLASS_NEW_IDEA = "NEW_IDEA"
CLASS_REPEATED = "REPEATED_IDEA"
CLASS_CHANGED = "CHANGED_VIEW"
CLASS_CONTRADICTION = "CONTRADICTION"
CLASS_TEMPORARY = "TEMPORARY_OPINION"

# Source Type Prefixes
SOURCE_VIDEO = "V"
SOURCE_PUBLIC_POST = "PC"
SOURCE_PAID_POST = "PP"
SOURCE_PDF = "D"
SOURCE_EXTERNAL = "E"

# Promotion Status
STATUS_IN_MASTER = "IN_MASTER"
STATUS_STAGED = "STAGED"
STATUS_RECENT_ONLY = "RECENT_ONLY"
STATUS_ARCHIVED = "ARCHIVED"

# File Paths (relative to repo root)
PATH_MASTER = "knowledge/01_Akshat_Master_System.md"
PATH_FREQUENCY = "knowledge/02_Akshat_Principle_Frequency_Table.md"
PATH_SOURCE_DB = "knowledge/03_Akshat_Source_Database.md"
PATH_RECENT = "knowledge/04_Akshat_Recent_Changes.md"
PATH_RAW_SOURCES = "raw_sources/"
PATH_INDEX = "raw_sources/index.json"
PATH_CHANGELOG = "changelog/CHANGELOG.md"

# Position Sizing Rules (from Master System)
MAX_SINGLE_STOCK_WEIGHT = 0.10   # 10% max per stock
MAX_HIGH_RISK_WEIGHT = 0.04      # 4% max for speculative positions
MIN_LIQUID_RATIO = 0.60          # 60% minimum liquid wealth target
MAX_ILLIQUID_RATIO = 0.25        # 25% max illiquid (real estate etc.)
MIN_DRY_POWDER = 0.05            # 5% minimum cash/dry powder

# Valuation Danger Zones
PE_EXTREME_WARNING = 60          # PE above this = extreme caution
PRICE_EARNINGS_CAGR_DIVERGENCE = 1.5   # Price CAGR / EPS CAGR ratio warning
