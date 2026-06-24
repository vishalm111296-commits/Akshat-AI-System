# Knowledge Graph Summary

## Entity Counts

Total Entities: 10

- **MacroTrend**: 2
- **Company**: 2
- **Sector**: 1
- **AssetClass**: 2
- **InvestmentPrinciple**: 2
- **Risk**: 1

## Relationship Counts

Total Relationships: 24

- **depends_on**: 24

## Top Connected Entities

- **GOLD**: 11 connections
- **INDIA_EQUITIES**: 11 connections
- **US_TECH**: 9 connections
- **DIVERSIFICATION**: 7 connections
- **AI_SUPERCYCLE**: 5 connections
- **INR_DEPRECIATION**: 3 connections
- **MICROSOFT**: 1 connections
- **BARBELL_PORTFOLIO**: 1 connections
- **NVIDIA**: 0 connections
- **DE_DOLLARIZATION**: 0 connections

## Entity Details

### AI_SUPERCYCLE

Type: MacroTrend

Relationships:

- depends_on US_TECH
- depends_on MICROSOFT


### NVIDIA

Type: Company

Relationships: None extracted



### MICROSOFT

Type: Company

Relationships: None extracted



### US_TECH

Type: Sector

Relationships:

- depends_on INDIA_EQUITIES
- depends_on DIVERSIFICATION


### GOLD

Type: AssetClass

Relationships:

- depends_on US_TECH
- depends_on INDIA_EQUITIES
- depends_on DIVERSIFICATION
- depends_on AI_SUPERCYCLE


### DE_DOLLARIZATION

Type: MacroTrend

Relationships: None extracted



### INDIA_EQUITIES

Type: AssetClass

Relationships:

- depends_on US_TECH
- depends_on GOLD
- depends_on DIVERSIFICATION


### BARBELL_PORTFOLIO

Type: InvestmentPrinciple

Relationships:

- depends_on GOLD


### DIVERSIFICATION

Type: InvestmentPrinciple

Relationships:

- depends_on GOLD
- depends_on INDIA_EQUITIES


### INR_DEPRECIATION

Type: Risk

Relationships:

- depends_on US_TECH
- depends_on INDIA_EQUITIES
- depends_on AI_SUPERCYCLE
