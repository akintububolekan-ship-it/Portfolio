#!/bin/bash

# Analytics scripts to insert
ANALYTICS_SCRIPT='
    <!-- Vercel Web Analytics -->
    <script>
      window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
    </script>
    <script defer src="/_vercel/insights/script.js"></script>
    
    <!-- Vercel Speed Insights -->
    <script>
      window.si = window.si || function () { (window.siq = window.siq || []).push(arguments); };
    </script>
    <script defer src="/_vercel/speed-insights/script.js"></script>
    '

# List of HTML files to update (excluding index.html which is already done)
FILES=(
  "articulate-project.html"
  "articulate.html"
  "baze-air.html"
  "bron-project.html"
  "bron.html"
  "caterpillar.html"
  "haystack-motion.html"
  "ifa-motion.html"
  "ifa-project.html"
  "ifa.html"
  "marigo-furnitures.html"
  "mkt.html"
  "no-mile.html"
  "numen.html"
  "openhouse-cinemas.html"
  "project.html"
  "radiant-glow.html"
  "rihub.html"
  "spendwise.html"
  "sprance-project.html"
  "sprance.html"
)

for file in "${FILES[@]}"; do
  if [ -f "$file" ]; then
    # Check if analytics is already added
    if ! grep -q "Vercel Web Analytics" "$file"; then
      # Insert analytics scripts before </head>
      sed -i "s|</head>|${ANALYTICS_SCRIPT}\n  </head>|" "$file"
      echo "✓ Added analytics to $file"
    else
      echo "- Analytics already present in $file"
    fi
  else
    echo "✗ File not found: $file"
  fi
done

echo ""
echo "Analytics installation complete!"
