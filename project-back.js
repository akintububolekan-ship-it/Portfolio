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

    // ===== Haptic & Audio Section Transition Feedback (iOS & Android) =====
    let audioCtx = null;
    let isAudioUnlocked = false;

    function initAudioSession() {
      // Set to 'ambient' so the browser naturally adopts the user's phone settings:
      // - Respects the hardware mute / silent switch (automatically silenced when phone is set to silent)
      // - Respects system ringer volume and lock state
      // - Mixes cleanly with any background audio/music without interrupting
      if (typeof navigator !== "undefined" && "audioSession" in navigator) {
        try {
          navigator.audioSession.type = "ambient";
        } catch (e) {}
      }
    }

    function getAudioContext() {
      if (!audioCtx) {
        initAudioSession();
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        if (AudioContextClass) {
          audioCtx = new AudioContextClass();
        }
      }
      return audioCtx;
    }

    function unlockAudio() {
      initAudioSession();
      const ctx = getAudioContext();
      if (!ctx) return;
      if (ctx.state === "suspended") {
        ctx.resume().catch(() => {});
      }
      // Essential iOS Safari hardware priming: play 1 silent sample synchronously during user touch
      if (!isAudioUnlocked) {
        try {
          const buf = ctx.createBuffer(1, 1, 22050);
          const src = ctx.createBufferSource();
          src.buffer = buf;
          src.connect(ctx.destination);
          src.start(0);
          isAudioUnlocked = true;
        } catch (e) {}
      }
    }

    // Listen to touch/pointer user gestures so iOS unlocks Web Audio immediately on first touch
    ["touchstart", "touchend", "touchmove", "pointerdown", "pointerup", "mousedown", "click", "keydown", "scroll"].forEach((evt) => {
      window.addEventListener(evt, unlockAudio, { passive: true });
    });

    function triggerHaptic() {
      // Respect user accessibility settings if reduced motion is requested
      if (typeof window !== "undefined" && window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        return;
      }

      // 1. Android & devices supporting the standard Vibration API
      // (The Android OS automatically adopts the user's system "Touch feedback / Haptics" and Silent/DND profile)
      try {
        if (typeof navigator !== "undefined" && navigator.vibrate) {
          navigator.vibrate([14]);
        }
      } catch (e) {}

      // 2. iOS 18+ Taptic Engine Workaround:
      // iOS WebKit triggers system Taptic Engine haptics when an HTML switch checkbox toggles
      try {
        const isIOS =
          /iPad|iPhone|iPod/.test(navigator.userAgent) ||
          (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);

        if (isIOS || !(typeof navigator !== "undefined" && navigator.vibrate)) {
          const label = document.createElement("label");
          label.setAttribute("aria-hidden", "true");
          label.style.cssText =
            "position:fixed;top:-9999px;left:-9999px;opacity:0;pointer-events:none;width:1px;height:1px;overflow:hidden;";

          const input = document.createElement("input");
          input.type = "checkbox";
          input.setAttribute("switch", "");
          label.appendChild(input);
          document.body.appendChild(label);

          // Force the iOS WebKit switch toggle to fire system Taptic Engine
          input.click();

          setTimeout(() => {
            try {
              label.remove();
            } catch (e) {}
          }, 60);
        }
      } catch (e) {}
    }

    function triggerTone(ctx) {
      try {
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        // Crisp, mechanical rotary dial click optimized for mobile/iPhone speakers:
        // Sweeps quickly from 850Hz down to 220Hz in 25ms so it resonates clearly through iPhone bottom speakers
        osc.type = "sine";
        osc.frequency.setValueAtTime(850, now);
        osc.frequency.exponentialRampToValueAtTime(220, now + 0.025);

        // Volume envelope scaled to 0.50 (50% amplitude) so output is exactly half of the volume the phone is set to:
        gain.gain.setValueAtTime(0.0001, now);
        gain.gain.linearRampToValueAtTime(0.5, now + 0.002);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.032);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(now);
        osc.stop(now + 0.032);
      } catch (e) {}
    }

    function playSectionFeedback() {
      // 1. Haptics (Vibration API on Android + Taptic Engine switch trigger on iOS)
      triggerHaptic();

      // 2. Audible subtle mechanical click (Web Audio + ambient audio routing respecting silent switch)
      try {
        const ctx = getAudioContext();
        if (!ctx) return;
        if (ctx.state === "suspended") {
          ctx.resume().then(() => {
            triggerTone(ctx);
          }).catch(() => {});
        } else {
          triggerTone(ctx);
        }
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
    let showMobileBubble = null;
    setupMobileSectionBubble();

    onSectionChangeCallback = (sec) => {
      if (window.innerWidth <= 1080 && sec && typeof showMobileBubble === "function") {
        showMobileBubble(sec, true);
      }
    };

    function setupMobileSectionBubble() {
      if (sections.length < 2) return;

      // Ensure any legacy secondary scroll wheel is removed
      const oldWheel = document.querySelector(".mobile-scroll-wheel");
      if (oldWheel) oldWheel.remove();

      // 1. Scroll Wheel Track and Thumb (The scroll wheel itself)
      let track = document.querySelector(".mobile-scroll-track");
      let thumb = document.querySelector(".mobile-scroll-thumb");
      if (!track) {
        track = document.createElement("div");
        track.className = "mobile-scroll-track";
        track.setAttribute("aria-hidden", "true");

        thumb = document.createElement("div");
        thumb.className = "mobile-scroll-thumb";
        thumb.setAttribute("role", "scrollbar");
        thumb.setAttribute("aria-label", "Case study scroll wheel");
        track.appendChild(thumb);
        document.body.appendChild(track);
      } else if (!thumb) {
        thumb = track.querySelector(".mobile-scroll-thumb");
      }

      // 2. Scroll Wheel Label Bubble
      let bubble = document.querySelector(".mobile-scroll-bubble");
      if (!bubble) {
        bubble = document.createElement("div");
        bubble.className = "mobile-scroll-bubble";
        bubble.setAttribute("role", "button");
        bubble.setAttribute("tabindex", "0");
        bubble.setAttribute("aria-label", "Scroll to next section");
        document.body.appendChild(bubble);
      }

      let titleSpan = bubble.querySelector(".mobile-scroll-bubble__title");
      let arrowSpan = bubble.querySelector(".mobile-scroll-bubble__arrow");
      if (!titleSpan) {
        bubble.innerHTML = `
          <span class="mobile-scroll-bubble__title"></span>
          <span class="mobile-scroll-bubble__arrow" aria-hidden="true">
            <svg viewBox="0 0 16 16" width="11" height="11" fill="none">
              <path d="M3.5 6l4.5 4.5 4.5-4.5" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </span>
        `;
        titleSpan = bubble.querySelector(".mobile-scroll-bubble__title");
        arrowSpan = bubble.querySelector(".mobile-scroll-bubble__arrow");
      }

      let fadeTimeout = null;

      function updatePositions() {
        const scrollY = window.scrollY;
        const docHeight = document.documentElement.scrollHeight;
        const winHeight = window.innerHeight;
        const maxScroll = Math.max(1, docHeight - winHeight);
        const ratio = Math.min(1, Math.max(0, scrollY / maxScroll));

        const thumbHeight = Math.max(38, Math.round((winHeight / docHeight) * winHeight));
        const maxTravel = winHeight - thumbHeight;
        const thumbTop = Math.min(maxTravel, Math.max(0, Math.round(ratio * maxTravel)));

        if (thumb) {
          thumb.style.height = `${thumbHeight}px`;
          thumb.style.transform = `translateY(${thumbTop}px)`;
        }

        if (bubble) {
          const thumbCenterY = thumbTop + (thumbHeight / 2);
          const clampedY = Math.min(winHeight - 28, Math.max(28, thumbCenterY));
          bubble.style.transform = `translateY(${clampedY}px) translateY(-50%)`;
        }
      }

      showMobileBubble = function (secInput, isSectionChange) {
        updatePositions();

        let text = "";
        let isLast = false;

        if (typeof secInput === "object" && secInput !== null) {
          text = secInput.text;
          isLast = secInput.id === sections[sections.length - 1].id;
        } else if (typeof secInput === "string") {
          text = secInput;
          isLast = sections[sections.length - 1].text.toLowerCase() === text.toLowerCase();
        } else {
          const curSec = sections.find((s) => s.id === lastActiveId) || sections[0];
          text = curSec.text;
          isLast = sections[sections.length - 1].id === curSec.id;
        }

        if (titleSpan) titleSpan.textContent = text;
        if (arrowSpan) {
          arrowSpan.innerHTML = isLast
            ? '<svg viewBox="0 0 16 16" width="11" height="11" fill="none"><path d="M3.5 10l4.5-4.5 4.5 4.5" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            : '<svg viewBox="0 0 16 16" width="11" height="11" fill="none"><path d="M3.5 6l4.5 4.5 4.5-4.5" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
        }

        bubble.setAttribute(
          "aria-label",
          isLast ? "Scroll back to top" : "Scroll to next section"
        );

        bubble.classList.add("mobile-scroll-bubble--visible");
        if (thumb) thumb.classList.add("mobile-scroll-thumb--visible");

        if (isSectionChange) {
          bubble.classList.add("mobile-scroll-bubble--pulse");
          setTimeout(() => {
            bubble.classList.remove("mobile-scroll-bubble--pulse");
          }, 180);
        }

        if (fadeTimeout) clearTimeout(fadeTimeout);
        if (!isInteracting && !isWheelInteracting && !isTouching) {
          scheduleFade();
        }
      };

      function scheduleFade() {
        if (fadeTimeout) clearTimeout(fadeTimeout);
        fadeTimeout = setTimeout(() => {
          bubble.classList.remove("mobile-scroll-bubble--visible");
          if (thumb) thumb.classList.remove("mobile-scroll-thumb--visible");
        }, 2000);
      }

      // ===== SCRUBBING ON THE SCROLL WHEEL ITSELF =====
      let isWheelInteracting = false;

      function scrubWheel(clientY) {
        const winHeight = window.innerHeight;
        const docHeight = document.documentElement.scrollHeight;
        const maxScroll = Math.max(1, docHeight - winHeight);
        const thumbHeight = Math.max(38, Math.round((winHeight / docHeight) * winHeight));
        const halfThumb = thumbHeight / 2;
        const availableTravel = Math.max(1, winHeight - thumbHeight);
        const ratio = Math.min(1, Math.max(0, (clientY - halfThumb) / availableTravel));
        window.scrollTo(0, ratio * maxScroll);
      }

      track.addEventListener("pointerdown", (e) => {
        if (e.button !== undefined && e.button !== 0) return;
        isWheelInteracting = true;
        if (thumb) {
          thumb.classList.add("mobile-scroll-thumb--active");
          thumb.classList.add("mobile-scroll-thumb--dragging");
        }
        try {
          track.setPointerCapture(e.pointerId);
        } catch (err) {}
        if (fadeTimeout) clearTimeout(fadeTimeout);
        scrubWheel(e.clientY);
        showMobileBubble(null, false);
      });

      track.addEventListener("pointermove", (e) => {
        if (!isWheelInteracting) return;
        e.preventDefault();
        scrubWheel(e.clientY);
      });

      function finishWheel(e) {
        if (!isWheelInteracting) return;
        isWheelInteracting = false;
        if (thumb) {
          thumb.classList.remove("mobile-scroll-thumb--active");
          thumb.classList.remove("mobile-scroll-thumb--dragging");
        }
        try {
          if (track.hasPointerCapture && track.hasPointerCapture(e.pointerId)) {
            track.releasePointerCapture(e.pointerId);
          }
        } catch (err) {}
        scheduleFade();
      }

      track.addEventListener("pointerup", finishWheel);
      track.addEventListener("pointercancel", finishWheel);

      // ===== CLICK & DRAG ON THE LABEL =====
      let lastAdvanceTime = 0;
      function safeAdvance() {
        const now = Date.now();
        if (now - lastAdvanceTime < 350) return;
        lastAdvanceTime = now;
        advanceToNextSection();
      }

      function advanceToNextSection() {
        const curIdx = sections.findIndex((s) => s.id === lastActiveId);
        if (curIdx >= 0 && curIdx < sections.length - 1) {
          const nextSec = sections[curIdx + 1];
          if (nextSec && nextSec.element) {
            const content = nextSec.element.closest(".project-content");
            if (content) {
              const collapsible = content.querySelector('[id$="-content"]');
              if (collapsible && collapsible.style.display === "none") {
                collapsible.style.display = "";
                const btn = content.querySelector(".section-header__action");
                if (btn) btn.textContent = "Close";
              }
            }
            const targetY = Math.max(0, nextSec.element.getBoundingClientRect().top + window.scrollY - 84);
            window.scrollTo({ top: targetY, behavior: "smooth" });
            setActive(nextSec.id, true);
          }
        } else {
          window.scrollTo({ top: 0, behavior: "smooth" });
          setActive(sections[0].id, true);
        }
      }

      let isInteracting = false;
      let hasDragged = false;
      let dragStartY = 0;

      bubble.addEventListener("pointerdown", (e) => {
        if (e.button !== undefined && e.button !== 0) return;
        isInteracting = true;
        hasDragged = false;
        dragStartY = e.clientY;
        bubble.classList.add("mobile-scroll-bubble--active");
        try {
          bubble.setPointerCapture(e.pointerId);
        } catch (err) {}
        if (fadeTimeout) clearTimeout(fadeTimeout);
      });

      bubble.addEventListener("pointermove", (e) => {
        if (!isInteracting) return;
        const deltaY = e.clientY - dragStartY;
        if (!hasDragged && Math.abs(deltaY) > 5) {
          hasDragged = true;
          bubble.classList.add("mobile-scroll-bubble--dragging");
        }
        if (hasDragged) {
          e.preventDefault();
          scrubWheel(e.clientY);
        }
      });

      function finishBubble(e) {
        if (!isInteracting) return;
        isInteracting = false;
        bubble.classList.remove("mobile-scroll-bubble--active");
        bubble.classList.remove("mobile-scroll-bubble--dragging");
        try {
          if (bubble.hasPointerCapture && bubble.hasPointerCapture(e.pointerId)) {
            bubble.releasePointerCapture(e.pointerId);
          }
        } catch (err) {}

        if (!hasDragged) {
          safeAdvance();
        }
        scheduleFade();
      }

      bubble.addEventListener("pointerup", finishBubble);
      bubble.addEventListener("pointercancel", finishBubble);

      bubble.addEventListener("click", (e) => {
        e.preventDefault();
        if (!hasDragged) {
          safeAdvance();
        }
        scheduleFade();
      });

      bubble.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          safeAdvance();
        }
      });

      // Window events for general scrolling & touch
      let isTouching = false;

      window.addEventListener("touchstart", () => {
        isTouching = true;
        const curSec = sections.find((s) => s.id === lastActiveId) || sections[0];
        if (curSec) {
          showMobileBubble(curSec, false);
        }
      }, { passive: true });

      window.addEventListener("touchend", () => {
        isTouching = false;
        if (!isInteracting && !isWheelInteracting) {
          scheduleFade();
        }
      }, { passive: true });

      window.addEventListener("touchcancel", () => {
        isTouching = false;
        if (!isInteracting && !isWheelInteracting) {
          scheduleFade();
        }
      }, { passive: true });

      window.addEventListener("scroll", () => {
        if (window.innerWidth > 1080) return;
        updatePositions();
        const curSec = sections.find((s) => s.id === lastActiveId) || sections[0];
        if (curSec) {
          showMobileBubble(curSec, false);
        }
      }, { passive: true });

      // Initialize bubble title and arrow on load
      showMobileBubble(sections[0], false);
    }
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
