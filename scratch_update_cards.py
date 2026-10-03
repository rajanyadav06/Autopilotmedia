with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Card 1: Performance Marketing
text = text.replace(
'''      <div class="service-card reveal">

        <div>

          <div class="service-card-top">

            <span class="service-num">
              01
            </span>

            <div class="service-icon-box">

              <!-- Target Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <circle
                  cx="12"
                  cy="12"
                  r="9"
                />

                <circle
                  cx="12"
                  cy="12"
                  r="5"
                />

                <circle
                  cx="12"
                  cy="12"
                  r="1"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
            Performance Marketing
          </h3>


          <p class="service-desc">
            Performance-focused Meta and Google campaigns built around
            your product, audience psychology, ROAS, CAC and profitability.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
            Meta & Google Ads
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </div>''',
'''      <a href="service-performance-marketing.html" class="service-card reveal">

        <div>

          <div class="service-card-top">

            <span class="service-num">
              01
            </span>

            <div class="service-icon-box">

              <!-- Target Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <circle
                  cx="12"
                  cy="12"
                  r="9"
                />

                <circle
                  cx="12"
                  cy="12"
                  r="5"
                />

                <circle
                  cx="12"
                  cy="12"
                  r="1"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
            Performance Marketing
          </h3>


          <p class="service-desc">
            Performance-focused Meta and Google campaigns built around
            your product, audience psychology, ROAS, CAC and profitability.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
            Meta & Google Ads
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </a>''')

# Card 2: Website Development
text = text.replace(
'''      <div
        class="service-card reveal"
        style="transition-delay: 0.1s;"
      >

        <div>

          <div class="service-card-top">

            <span class="service-num">
              02
            </span>

            <div class="service-icon-box">

              <!-- Browser Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <rect
                  x="3"
                  y="4"
                  width="18"
                  height="16"
                  rx="2"
                />

                <line
                  x1="3"
                  y1="9"
                  x2="21"
                  y2="9"
                />

                <circle
                  cx="7"
                  cy="6.5"
                  r=".5"
                  fill="currentColor"
                />

                <circle
                  cx="10"
                  cy="6.5"
                  r=".5"
                  fill="currentColor"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
            Website Development
          </h3>


          <p class="service-desc">
            Fast, conversion-focused Shopify and custom websites
            designed to turn traffic into customers across every device.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
            Shopify & Custom
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </div>''',
'''      <a href="service-website-development.html"
        class="service-card reveal"
        style="transition-delay: 0.1s;"
      >

        <div>

          <div class="service-card-top">

            <span class="service-num">
              02
            </span>

            <div class="service-icon-box">

              <!-- Browser Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <rect
                  x="3"
                  y="4"
                  width="18"
                  height="16"
                  rx="2"
                />

                <line
                  x1="3"
                  y1="9"
                  x2="21"
                  y2="9"
                />

                <circle
                  cx="7"
                  cy="6.5"
                  r=".5"
                  fill="currentColor"
                />

                <circle
                  cx="10"
                  cy="6.5"
                  r=".5"
                  fill="currentColor"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
            Website Development
          </h3>


          <p class="service-desc">
            Fast, conversion-focused Shopify and custom websites
            designed to turn traffic into customers across every device.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
            Shopify & Custom
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </a>''')

# Card 3: Social Media Management
text = text.replace(
'''      <div
        class="service-card reveal"
        style="transition-delay: 0.2s;"
      >

        <div>

          <div class="service-card-top">

            <span class="service-num">
              03
            </span>

            <div class="service-icon-box">

              <!-- Social / Share Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <circle
                  cx="18"
                  cy="5"
                  r="3"
                />

                <circle
                  cx="6"
                  cy="12"
                  r="3"
                />

                <circle
                  cx="18"
                  cy="19"
                  r="3"
                />

                <line
                  x1="8.6"
                  y1="13.5"
                  x2="15.4"
                  y2="17.5"
                />

                <line
                  x1="15.4"
                  y1="6.5"
                  x2="8.6"
                  y2="10.5"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
            Social Media Management
          </h3>


          <p class="service-desc">
            Strategic social content designed around your brand,
            audience and purchase intent—not vanity engagement.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
            Social Growth
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </div>''',
'''      <a href="service-social-media.html"
        class="service-card reveal"
        style="transition-delay: 0.2s;"
      >

        <div>

          <div class="service-card-top">

            <span class="service-num">
              03
            </span>

            <div class="service-icon-box">

              <!-- Social / Share Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <circle
                  cx="18"
                  cy="5"
                  r="3"
                />

                <circle
                  cx="6"
                  cy="12"
                  r="3"
                />

                <circle
                  cx="18"
                  cy="19"
                  r="3"
                />

                <line
                  x1="8.6"
                  y1="13.5"
                  x2="15.4"
                  y2="17.5"
                />

                <line
                  x1="15.4"
                  y1="6.5"
                  x2="8.6"
                  y2="10.5"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
            Social Media Management
          </h3>


          <p class="service-desc">
            Strategic social content designed around your brand,
            audience and purchase intent—not vanity engagement.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
            Social Growth
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </a>''')

# Card 4: Content Creation
text = text.replace(
'''      <div class="service-card reveal">

        <div>

          <div class="service-card-top">

            <span class="service-num">
              04
            </span>

            <div class="service-icon-box">

              <!-- Sparkle Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <path
                  d="M12 2
                     L14.2 8.8
                     L21 11
                     L14.2 13.2
                     L12 20
                     L9.8 13.2
                     L3 11
                     L9.8 8.8
                     Z"
                />

                <path
                  d="M19 3v4"
                />

                <path
                  d="M21 5h-4"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
            Content Creation
          </h3>


          <p class="service-desc">
            Reels, ads, creative concepts, hooks and visual content
            produced with a D2C and performance-growth mindset.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
            Reels & Ad Creatives
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </div>''',
'''      <a href="service-content-creation.html" class="service-card reveal">

        <div>

          <div class="service-card-top">

            <span class="service-num">
              04
            </span>

            <div class="service-icon-box">

              <!-- Sparkle Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <path
                  d="M12 2
                     L14.2 8.8
                     L21 11
                     L14.2 13.2
                     L12 20
                     L9.8 13.2
                     L3 11
                     L9.8 8.8
                     Z"
                />

                <path
                  d="M19 3v4"
                />

                <path
                  d="M21 5h-4"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
            Content Creation
          </h3>


          <p class="service-desc">
            Reels, ads, creative concepts, hooks and visual content
            produced with a D2C and performance-growth mindset.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
            Reels & Ad Creatives
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </a>''')

# Card 5: SEO / AEO / GEO
text = text.replace(
'''      <div
        class="service-card reveal"
        style="transition-delay: 0.1s;"
      >

        <div>

          <div class="service-card-top">

            <span class="service-num">
              05
            </span>

            <div class="service-icon-box">

              <!-- Search Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <circle
                  cx="11"
                  cy="11"
                  r="7"
                />

                <line
                  x1="16"
                  y1="16"
                  x2="21"
                  y2="21"
                />

                <path
                  d="M8 11h6"
                />

                <path
                  d="M11 8v6"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
            SEO / AEO / GEO
          </h3>


          <p class="service-desc">
            Search strategies built to bring qualified, bottom-funnel
            traffic through traditional search and AI-powered discovery.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
            Search & AI Visibility
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </div>''',
'''      <a href="service-seo-aeo-geo.html"
        class="service-card reveal"
        style="transition-delay: 0.1s;"
      >

        <div>

          <div class="service-card-top">

            <span class="service-num">
              05
            </span>

            <div class="service-icon-box">

              <!-- Search Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <circle
                  cx="11"
                  cy="11"
                  r="7"
                />

                <line
                  x1="16"
                  y1="16"
                  x2="21"
                  y2="21"
                />

                <path
                  d="M8 11h6"
                />

                <path
                  d="M11 8v6"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
            SEO / AEO / GEO
          </h3>


          <p class="service-desc">
            Search strategies built to bring qualified, bottom-funnel
            traffic through traditional search and AI-powered discovery.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
            Search & AI Visibility
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </a>''')

# Card 6: Influencer Marketing
text = text.replace(
'''      <div
        class="service-card reveal"
        style="transition-delay: 0.2s;"
      >

        <div>

          <div class="service-card-top">

            <span class="service-num">
              06
            </span>

            <div class="service-icon-box">

              <!-- Users / Creator Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <circle
                  cx="9"
                  cy="8"
                  r="3"
                />

                <path
                  d="M3 20
                     C3 16.7 5.7 14 9 14
                     C12.3 14 15 16.7 15 20"
                />

                <circle
                  cx="17"
                  cy="8"
                  r="2.5"
                />

                <path
                  d="M15 14.5
                     C18.5 14.5 21 16.8 21 20"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
            Influencer Marketing
          </h3>


          <p class="service-desc">
            Creator collaborations planned around product fit,
            audience relevance and measurable campaign outcomes.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
            Creator Partnerships
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </div>''',
'''      <a href="service-influencer-marketing.html"
        class="service-card reveal"
        style="transition-delay: 0.2s;"
      >

        <div>

          <div class="service-card-top">

            <span class="service-num">
              06
            </span>

            <div class="service-icon-box">

              <!-- Users / Creator Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <circle
                  cx="9"
                  cy="8"
                  r="3"
                />

                <path
                  d="M3 20
                     C3 16.7 5.7 14 9 14
                     C12.3 14 15 16.7 15 20"
                />

                <circle
                  cx="17"
                  cy="8"
                  r="2.5"
                />

                <path
                  d="M15 14.5
                     C18.5 14.5 21 16.8 21 20"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
            Influencer Marketing
          </h3>


          <p class="service-desc">
            Creator collaborations planned around product fit,
            audience relevance and measurable campaign outcomes.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
            Creator Partnerships
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </a>''')

# Card 7: AI Automation
text = text.replace(
'''       <div
        class="service-card reveal"
        style="transition-delay: 0.2s;"
      >

        <div>

          <div class="service-card-top">

            <span class="service-num">
              07
            </span>

            <div class="service-icon-box">

              <!-- Users / Creator Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <circle
                  cx="9"
                  cy="8"
                  r="3"
                />

                <path
                  d="M3 20
                     C3 16.7 5.7 14 9 14
                     C12.3 14 15 16.7 15 20"
                />

                <circle
                  cx="17"
                  cy="8"
                  r="2.5"
                />

                <path
                  d="M15 14.5
                     C18.5 14.5 21 16.8 21 20"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
             AI Automation
          </h3>


          <p class="service-desc">
             AI-powered workflows that automate repetitive tasks,
      lead management, customer support and business operations.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
             AI & Business Automation
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </div>''',
'''       <a href="service-ai-automation.html"
        class="service-card reveal"
        style="transition-delay: 0.2s;"
      >

        <div>

          <div class="service-card-top">

            <span class="service-num">
              07
            </span>

            <div class="service-icon-box">

              <!-- Users / Creator Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <circle
                  cx="9"
                  cy="8"
                  r="3"
                />

                <path
                  d="M3 20
                     C3 16.7 5.7 14 9 14
                     C12.3 14 15 16.7 15 20"
                />

                <circle
                  cx="17"
                  cy="8"
                  r="2.5"
                />

                <path
                  d="M15 14.5
                     C18.5 14.5 21 16.8 21 20"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
             AI Automation
          </h3>


          <p class="service-desc">
             AI-powered workflows that automate repetitive tasks,
      lead management, customer support and business operations.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
             AI & Business Automation
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </a>''')

# Card 8: Landing Page
text = text.replace(
'''       <div
        class="service-card reveal"
        style="transition-delay: 0.2s;"
      >

        <div>

          <div class="service-card-top">

            <span class="service-num">
              08
            </span>

            <div class="service-icon-box">

              <!-- Users / Creator Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <circle
                  cx="9"
                  cy="8"
                  r="3"
                />

                <path
                  d="M3 20
                     C3 16.7 5.7 14 9 14
                     C12.3 14 15 16.7 15 20"
                />

                <circle
                  cx="17"
                  cy="8"
                  r="2.5"
                />

                <path
                  d="M15 14.5
                     C18.5 14.5 21 16.8 21 20"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
             Landing Page
          </h3>


          <p class="service-desc">
             High-converting landing pages designed around your
      offer, audience, messaging and campaign goals.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
             Conversion-Focused Pages
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </div>''',
'''       <a href="service-landing-page-cro.html"
        class="service-card reveal"
        style="transition-delay: 0.2s;"
      >

        <div>

          <div class="service-card-top">

            <span class="service-num">
              08
            </span>

            <div class="service-icon-box">

              <!-- Users / Creator Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <circle
                  cx="9"
                  cy="8"
                  r="3"
                />

                <path
                  d="M3 20
                     C3 16.7 5.7 14 9 14
                     C12.3 14 15 16.7 15 20"
                />

                <circle
                  cx="17"
                  cy="8"
                  r="2.5"
                />

                <path
                  d="M15 14.5
                     C18.5 14.5 21 16.8 21 20"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
             Landing Page
          </h3>


          <p class="service-desc">
             High-converting landing pages designed around your
      offer, audience, messaging and campaign goals.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
             Conversion-Focused Pages
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </a>''')

# Card 9: CRO
text = text.replace(
'''       <div
        class="service-card reveal"
        style="transition-delay: 0.2s;"
      >

        <div>

          <div class="service-card-top">

            <span class="service-num">
              09
            </span>

            <div class="service-icon-box">

              <!-- Users / Creator Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <circle
                  cx="9"
                  cy="8"
                  r="3"
                />

                <path
                  d="M3 20
                     C3 16.7 5.7 14 9 14
                     C12.3 14 15 16.7 15 20"
                />

                <circle
                  cx="17"
                  cy="8"
                  r="2.5"
                />

                <path
                  d="M15 14.5
                     C18.5 14.5 21 16.8 21 20"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
                CRO
          </h3>


          <p class="service-desc">
               Conversion rate optimization focused on improving
      user experience, reducing friction and turning more
      visitors into customers.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
             Conversion Rate Optimization
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </div>''',
'''       <a href="service-landing-page-cro.html"
        class="service-card reveal"
        style="transition-delay: 0.2s;"
      >

        <div>

          <div class="service-card-top">

            <span class="service-num">
              09
            </span>

            <div class="service-icon-box">

              <!-- Users / Creator Icon -->

              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >

                <circle
                  cx="9"
                  cy="8"
                  r="3"
                />

                <path
                  d="M3 20
                     C3 16.7 5.7 14 9 14
                     C12.3 14 15 16.7 15 20"
                />

                <circle
                  cx="17"
                  cy="8"
                  r="2.5"
                />

                <path
                  d="M15 14.5
                     C18.5 14.5 21 16.8 21 20"
                />

              </svg>

            </div>

          </div>


          <h3 class="service-title">
                CRO
          </h3>


          <p class="service-desc">
               Conversion rate optimization focused on improving
      user experience, reducing friction and turning more
      visitors into customers.
          </p>

        </div>


        <div class="service-card-bottom">

          <span class="service-learn-more">
             Conversion Rate Optimization
          </span>

          <span class="service-arrow">
            →
          </span>

        </div>

      </a>''')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated index.html service cards successfully!")
