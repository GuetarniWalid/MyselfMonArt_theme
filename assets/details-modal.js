class DetailsModal extends HTMLElement {
  constructor() {
    super();
    this.detailsContainer = this.querySelector('details');
    this.summaryToggle = this.querySelector('summary');

    this.detailsContainer.addEventListener('keyup', event => event.code.toUpperCase() === 'ESCAPE' && this.close());
    this.summaryToggle.addEventListener('click', this.onSummaryClick.bind(this));
    this.querySelector('button[type="button"]').addEventListener('click', this.close.bind(this));

    this.summaryToggle.setAttribute('role', 'button');
  }

  connectedCallback() {
    const overlay = this.querySelector('.modal-overlay')
    overlay.addEventListener('mouseenter', () => {
      document.cursorInCartButton = true
    });
    overlay.addEventListener('mouseleave', () => {
      document.cursorInCartButton = false
    });
  }

  isOpen() {
    return this.detailsContainer.hasAttribute('open');
  }

  onSummaryClick(event) {
    event.preventDefault();
    event.target.closest('details').hasAttribute('open') ? this.close() : this.open(event);
  }

  onBodyClick(event) {
    if (!this.contains(event.target) || event.target.classList.contains('modal-overlay')) this.close(false);
  }

  open(event) {
    this.onBodyClickEvent = this.onBodyClickEvent || this.onBodyClick.bind(this);
    event.target.closest('details').setAttribute('open', true);
    document.body.addEventListener('click', this.onBodyClickEvent);
    document.body.classList.add('overflow-hidden');
    this.closest('.header__icons').nextElementSibling?.classList.add('hidden');

    trapFocus(this.detailsContainer.querySelector('[tabindex="-1"]'), this.detailsContainer.querySelector('input:not([type="hidden"])'));
  }

  close(focusToggle = true) {
    removeTrapFocus(focusToggle ? this.summaryToggle : null);
    this.detailsContainer.removeAttribute('open');
    document.body.removeEventListener('click', this.onBodyClickEvent);
    document.body.classList.remove('overflow-hidden');
    this.closest('.header__icons').nextElementSibling?.classList.remove('hidden');
  }
}
customElements.define('details-modal', DetailsModal);

class FixedLoup extends HTMLElement {
  constructor() {
    super()
    this.querySelector('button').addEventListener('click', this.onClick.bind(this));
  }

  onClick(event) {
    event.stopPropagation()
    document.querySelector('header details-modal').querySelector('summary').click();
    document.querySelector('sticky-header').reveal();
  }
}
customElements.define('fixed-loup', FixedLoup);
