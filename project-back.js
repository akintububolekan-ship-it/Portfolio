(function () {
  function setupBackLink() {
    const backLink = document.querySelector(".project-header__back");
    if (!backLink) return;
    try {
      const savedTab =
        sessionStorage.getItem("portfolioActiveTab") ||
        localStorage.getItem("portfolioActiveTab");
      if (savedTab) {
        backLink.setAttribute("href", "index.html#" + savedTab);
      }
    } catch (e) {}
    backLink.addEventListener("click", (e) => {
      if (
        window.history.length > 1 &&
        document.referrer &&
        document.referrer.includes(window.location.host)
      ) {
        e.preventDefault();
        window.history.back();
      }
    });
  }

  function setupCaseStudyNav() {
    const main = document.querySelector(".project-page");
    if (!main) return;

    // Select all h2 section headings within the case study
    const allHeadings = Array.from(main.querySelectorAll(".project-content h2, .project-text h2, h2"));
    const headings = [];
    const seen = new Set();
    allHeadings.forEach((h2) => {
      if (!seen.has(h2) && h2.closest(".project-page")) {
        seen.add(h2);
        headings.push(h2);
      }
    });

    if (headings.length === 0) return;

    const sections = [];
    headings.forEach((h2, index) => {
      // Clean up text: remove any "Close" or "View" button text
      const clone = h2.cloneNode(true);
      const actionBtn = clone.querySelector(".section-header__action, button");
      if (actionBtn) actionBtn.remove();
      const rawText = clone.textContent.replace(/\b(Close|View)\b/gi, "").trim();
      if (!rawText) return;

      // Assign an id if missing
      let id = h2.id;
      if (!id) {
        id = "sec-" + rawText.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
        if (document.getElementById(id)) {
          id += "-" + (index + 1);
        }
        h2.id = id;
      }
      h2.style.scrollMarginTop = "84px";

      sections.push({
        id: id,
        text: rawText,
        element: h2
      });
    });

    if (sections.length < 2) return;

    // Check if nav already exists
    let nav = document.querySelector(".case-study-nav");
    if (!nav) {
      nav = document.createElement("nav");
      nav.className = "case-study-nav";
      nav.setAttribute("aria-label", "Case study navigation");
      document.body.appendChild(nav);
    } else {
      nav.innerHTML = "";
    }

    const links = [];
    sections.forEach((sec, idx) => {
      const a = document.createElement("a");
      a.className = "case-study-nav__link" + (idx === 0 ? " case-study-nav__link--active" : "");
      a.href = "#" + sec.id;
      a.setAttribute("data-target-id", sec.id);
      a.textContent = sec.text;

      a.addEventListener("click", (e) => {
        e.preventDefault();
        const target = document.getElementById(sec.id);
        if (target) {
          // If the section is inside a collapsed container, open it!
          const content = target.closest(".project-content");
          if (content) {
            const collapsible = content.querySelector('[id$="-content"]');
            if (collapsible && collapsible.style.display === "none") {
              collapsible.style.display = "";
              const btn = content.querySelector(".section-header__action");
              if (btn) btn.textContent = "Close";
            }
          }
          target.scrollIntoView({ behavior: "smooth", block: "start" });
          setActive(sec.id);
        }
      });

      nav.appendChild(a);
      links.push(a);
    });

    // ===== Haptic & Audio Section Transition Feedback =====
    let audioCtx = null;
    function getAudioContext() {
      if (!audioCtx) {
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        if (AudioContextClass) {
          audioCtx = new AudioContextClass();
        }
      }
      if (audioCtx && audioCtx.state === "suspended") {
        audioCtx.resume().catch(() => {});
      }
      return audioCtx;
    }

    function unlockAudio() {
      const ctx = getAudioContext();
      if (ctx && ctx.state === "suspended") {
        ctx.resume().catch(() => {});
      }
    }
    ["scroll", "pointerdown", "touchstart", "keydown"].forEach((evt) => {
      window.addEventListener(evt, unlockAudio, { passive: true, once: true });
    });

    function playSectionFeedback() {
      // 1. Very low vibration (8ms subtle haptic pulse)
      try {
        if (typeof navigator !== "undefined" && navigator.vibrate) {
          navigator.vibrate(8);
        }
      } catch (e) {}

      // 2. Very low & subtle tick sound (low frequency, soft volume)
      try {
        const ctx = getAudioContext();
        if (!ctx) return;
        if (ctx.state === "suspended") {
          ctx.resume().catch(() => {});
        }

        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        // Soft, low-frequency notch tick (150Hz decaying to 55Hz in 30ms)
        osc.type = "sine";
        osc.frequency.setValueAtTime(150, now);
        osc.frequency.exponentialRampToValueAtTime(55, now + 0.03);

        // Very low volume (0.032) quickly fading out
        gain.gain.setValueAtTime(0.032, now);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.035);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(now);
        osc.stop(now + 0.035);
      } catch (e) {}
    }

    let lastActiveId = null;
    let isInitialLoad = true;
    let onSectionChangeCallback = null;

    function setActive(activeId, triggerFeedback) {
      if (activeId === lastActiveId) return;

      if (triggerFeedback && !isInitialLoad && lastActiveId !== null) {
        playSectionFeedback();
      }

      lastActiveId = activeId;
      isInitialLoad = false;

      links.forEach((a) => {
        if (a.getAttribute("data-target-id") === activeId) {
          a.classList.add("case-study-nav__link--active");
        } else {
          a.classList.remove("case-study-nav__link--active");
        }
      });

      if (typeof onSectionChangeCallback === "function") {
        const secObj = sections.find((s) => s.id === activeId);
        if (secObj) onSectionChangeCallback(secObj);
      }
    }

    // Scrollspy to highlight active link
    let isTicking = false;
    function onScrollSpy() {
      if (isTicking) return;
      isTicking = true;
      requestAnimationFrame(() => {
        const scrollY = window.scrollY;
        const offset = 140;

        // If near bottom of the page, activate the last section
        if (window.innerHeight + scrollY >= document.documentElement.scrollHeight - 60) {
          setActive(sections[sections.length - 1].id, true);
          isTicking = false;
          return;
        }

        // Find which section is currently active
        let currentId = sections[0].id;
        for (let i = 0; i < sections.length; i++) {
          const rect = sections[i].element.getBoundingClientRect();
          if (rect.top <= offset) {
            currentId = sections[i].id;
          } else {
            break;
          }
        }
        setActive(currentId, true);
        isTicking = false;
      });
    }

    window.addEventListener("scroll", onScrollSpy, { passive: true });
    setActive(sections[0].id, false);

    // ===== MOBILE SECTION INDICATOR BUBBLE (ATTACHED TO MAIN SCROLL) =====
    setupMobileSectionBubble(sections, (activeSec) => {
      if (window.innerWidth <= 1080 && activeSec) {
        showMobileBubble(activeSec.text);
      }
    });

    onSectionChangeCallback = (sec) => {
      if (window.innerWidth <= 1080 && sec && typeof showMobileBubble === "function") {
        showMobileBubble(sec.text);
      }
    };
  }

  let showMobileBubble = null;

  function setupMobileSectionBubble(sections) {
    if (sections.length < 2) return;

    // Remove any legacy secondary scroll wheel if present
    const oldWheel = document.querySelector(".mobile-scroll-wheel");
    if (oldWheel) oldWheel.remove();

    let bubble = document.querySelector(".mobile-scroll-bubble");
    if (!bubble) {
      bubble = document.createElement("div");
      bubble.className = "mobile-scroll-bubble";
      document.body.appendChild(bubble);
    }

    let fadeTimeout = null;

    function updateBubbleVerticalPosition() {
      const scrollY = window.scrollY;
      const docHeight = document.documentElement.scrollHeight;
      const winHeight = window.innerHeight;
      const maxScroll = Math.max(1, docHeight - winHeight);
      const ratio = Math.min(1, Math.max(0, scrollY / maxScroll));

      // Estimated native mobile scrollbar thumb travel range
      const thumbHeight = Math.max(36, (winHeight / docHeight) * winHeight);
      const maxTravel = winHeight - thumbHeight;
      const thumbCenterY = (ratio * maxTravel) + (thumbHeight / 2);

      // Clamp between padding so it doesn't touch screen top or bottom
      const clampedY = Math.min(winHeight - 28, Math.max(28, thumbCenterY));
      bubble.style.transform = `translateY(${clampedY}px) translateY(-50%)`;
    }

    showMobileBubble = function(text) {
      updateBubbleVerticalPosition();
      bubble.textContent = text;
      bubble.classList.add("mobile-scroll-bubble--visible");
      if (fadeTimeout) clearTimeout(fadeTimeout);
      if (!isTouching) {
        scheduleBubbleFade();
      }
    };

    function scheduleBubbleFade() {
      if (fadeTimeout) clearTimeout(fadeTimeout);
      fadeTimeout = setTimeout(() => {
        bubble.classList.remove("mobile-scroll-bubble--visible");
      }, 3000);
    }

    // Connect to scroll and touch activity on mobile
    let isTouching = false;

    window.addEventListener("touchstart", () => {
      isTouching = true;
      const activeLink = document.querySelector(".case-study-nav__link--active");
      if (activeLink) {
        showMobileBubble(activeLink.textContent.trim());
      }
    }, { passive: true });

    window.addEventListener("touchend", () => {
      isTouching = false;
      scheduleBubbleFade();
    }, { passive: true });

    window.addEventListener("touchcancel", () => {
      isTouching = false;
      scheduleBubbleFade();
    }, { passive: true });

    // When scrolling on mobile (finger swipe or mouse wheel)
    window.addEventListener("scroll", () => {
      if (window.innerWidth > 1080) return;
      updateBubbleVerticalPosition();
      const activeLink = document.querySelector(".case-study-nav__link--active");
      if (activeLink) {
        showMobileBubble(activeLink.textContent.trim());
      }
    }, { passive: true });
  }

  function init() {
    setupBackLink();
    setupCaseStudyNav();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
